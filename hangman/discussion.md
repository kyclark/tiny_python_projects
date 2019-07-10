As suggested in the specs, I put all the validation of user inputs into my `get_args` function, relying on `argparse` to validate that the `--wordlist` is a readable file and using `parser.error` to throw any problems with `--minlen` and `--maxlen`. By the time I have my `args` from `get_args`, I know I have all the right types and values for my inputs. I immediately set `random.seed` with the value of `args.seed` knowing that it is either a valid `int` or the `None` value which is essentially the same as not setting the seed.

## Getting the words

This program assumes a dictionary-type file like the standard `/usr/share/dict/words` file with words and no punctuation, so I use `read().lower().split()` to read the wordlist argument which will be an open file handle because of how I defined it with `argparse`. I decided to write a small function to read the file:

````
def get_words(wordlist, min_len, max_len):
    good = '^[a-z]{' + str(min_len) + ',' + str(max_len) + '}$'
    is_good = lambda w: re.match(good, w)
    return list(filter(is_good, wordlist.read().lower().split()))
````

I can run my function to see if it works, faking an open file handle using `io.StringIO`:

````
>>> import re, io
>>> text = 'Apple banana COW da epinephrine'
>>> get_words(io.StringIO(text), 1, 20)
['apple', 'banana', 'cow', 'da', 'epinephrine']
>>> get_words(io.StringIO(text), 5, 10)
['apple', 'banana']
````

And then I can write a `test_get_words` function:

````
>>> def test_get_words():
...     text = 'Apple banana COW da epinephrine'
...     assert get_words(io.StringIO(text), 1, 20) == text.lower().split()
...     assert get_words(io.StringIO(text), 5, 10) == ['apple', 'banana']
...     assert get_words(io.StringIO(text), 3, 10) == ['apple', 'banana', 'cow']
...
````

## Selecting a word

Once I have my `words`, I use `random.choice` to make a selection:

````
>>> import random
>>> random.seed(1)
>>> word = random.choice(get_words(io.StringIO(text), 1, 20))
>>> word
'banana'
````

## Recursion vs Infinite Loops

From here, I could use the normal `while True` idiom to create an infinite loop from which I can `break` when the game is over or `continue` when I want to skip to the next iteration. For this example, I wanted to show how to write a *recursive* function -- a function that calls itself, like a snake head eating the head on the opposite side. I have two reasons to do this:

1. I want to avoid using variables outside the loop to maintain the "state" of the program
2. Recursive functions are cool and it's fun to play with them

For what it's worth, my experience programming web interfaces with the Elm language (a dialect of Haskell that compiles to JavaScript) greatly influenced my decision to write the program this way. In Elm, there is a single `Model` that holds the state of the program where "state" means the values of everything in the program. There is a single `update` function that changes the state which is immediately followed by a `view` function to show the current state of the program.

## Maintaining state

For our "Hangman," we need to keep track of the following:

1. The randomly selected word that is being guessed
2. The letters of the word which have been correctly guessed
3. The letters the user guessed which were not found in the word
4. The number of misses the user had made
5. The maximum number of misses the user is allowed
6. Any characters provided for the `inputs`

I *could* create 6 variables outside of a `while` loop and mutate those each time through the loop to know how the game is progressing. Instead, I created the function `play` and pass in a `dict` that holds all these values. It's perhaps the single longest function in the book running just over 60 lines. I usually try to keep every function short enough to fit into 80 characters wide and 50 lines long (the default size of my terminal windows). I strongly believe you should be able to see the entire function in one screen, but this one needs to be just a little longer.

## Shall we play a game?

I wrote `play` to eventually `return` either `True` or `False` to indicate if the user won or not. I want to show you another way to debug a program. If you are in the same directory as your `hangman.py` program (and you created it with the `new.py` so that it has the `if __name__ == '__main__'` bit so that it won't immediately try to execute code), then you can actually `import` your entire program and `play` the game like so:

````
>>> import hangman
>>> hangman.play({'word': 'banana'})
_ _ _ _ _ _ (Misses: 0)
Your guess? ("?" for hint, "!" to quit) a
_ a _ a _ a (Misses: 0)
Your guess? ("?" for hint, "!" to quit) b
b a _ a _ a (Misses: 0)
Your guess? ("?" for hint, "!" to quit) n
You guessed "banana" with "0" misses.
True
````

Or pass in the `inputs`:

````
>>> hangman.play({'word': 'banana', 'inputs': list('ban')})
_ _ _ _ _ _ (Misses: 0)
b _ _ _ _ _ (Misses: 0)
b a _ a _ a (Misses: 0)
You guessed "banana" with "0" misses.
True
````

Now, how can I write a `play` to do that? The function takes just one argument which I call `state` which is a regular `dict` to hold key/value pairs. As I demonstrate above, not all of the 6 variables listed above need to be passed in for it to work. I use the `dict.get` function to return the `value` for a given `key` if the `key` exists, otherwise return a default value passed as the second argument:

````
>>> state = {'word': 'banana', 'inputs': list('ban')}
>>> guessed = state.get('guessed', list('_' * len(word)))
>>> guessed
['_', '_', '_', '_', '_', '_']
````

Here I represent the state of those letters that have been guessed or not as a string the same length as the `word` where there are underscores (`_`) for letters not yet guessed and those which have been guessed are present in their correct locations.

The previous guesses I store as a `set` because I only care about the unique letters:

````
>>> prev_guesses = state.get('prev_guesses', set())
>>> prev_guesses
set()
````

The default value for the number of misses is `0`:

````
>>> num_misses = state.get('num_misses', 0)
>>> num_misses
0
````

And the upper limit for maximum guesses is `10`:

````
>>> max_misses = state.get('max_misses', 10)
>>> max_misses
10
````

Finally, the `inputs` will default to an empty `list`:

````
>>> inputs = state.get('inputs', [])
>>> inputs
['b', 'a', 'n']
````

First I check if the `guessed` is the same as the `word`. If so, the user has won and I can `return True` to indicate this. Right now, this is not so:

````
>>> ''.join(guessed) == word
False
````

Then I check if they have guessed too many times:

````
>>> num_misses >= max_misses
False
````

So far, so good. Now I either want to get some character from the user for the next guessed letter or take it from the `inputs`:

````
>>> get_char = lambda: input('Your guess? ("?" for hint, "!" to quit) ').lower()
>>> new_guess = inputs.pop(0) if inputs else get_char()
>>> new_guess
'b'
````

The `lambda` is to create an function that I can call with `get_char()` if I need it. I could have written it all on one line, but I detest lines over 80 characters.

The user is allowed to exit the game early with a `!`, so I check if the `new_guess` is that and `return False` if so. They can also request a free letter with `?`. To select a free letter, I need to choose from the letters in the `word` if they are not present in the ones that have been `guessed`:

````
>>> new_guess = random.choice([c for c in word if c not in guessed])
>>> new_guess
'n'
````

At this point, I should have something from the user, whether they responded to the `input` or I took it from the `inputs` or they requested a hint. I need to verify that they gave me something that looks like just one character from the set `a-z`. I hope you immediately think of using a regular expression with a character class:

````
>>> re.match('^[a-z]$', new_guess)
<re.Match object; span=(0, 1), match='n'>
````

Where the caret (`^`) will anchor the regex to the start of the string, the `[a-z]` creates a character class comprised only of the lowercase letters from `a` to `z`, and the `$` anchors the pattern to the end of the string. Because I didn't indicate any number of matches with `*` (zero or more) or `+` (one or more) or `{n}` (`n` exactly), etc. it will match only one character. If this *fails* to match, then we do not have a valid input.

I check if `new_guess in prev_guesses` and let the user know if that is so. Then I check if `new_guess in word`. If so, they have guessed a letter correctly! I need to update the `guessed` list with the `new_guess` using the positions of that letter in the `word`. This is a bit tricky, and perhaps you chose to handle this differently. Here's what I do.

Let's say the `word='banana'` and `new_guess='n'`. I need to know the positions of `'n'` in `'banana'`:

````
>>> word
'banana'
>>> word.find('n')
2
````

Yes, there is an "n" at index 2:

````
>>> word[2]
'n'
````

So I can update `guessed` with that information:

````
>>> guessed
['_', '_', '_', '_', '_', '_']
>>> guessed[2] = 'n'
>>> guessed
['_', '_', 'n', '_', '_', '_']
````

If I call `word.find('n')` again, I'll get `2` again because it always starts searching from the beginning of the string. Note that `str.index` works the same way. I can pass a second optional argument to indicate the starting search index. Note that this need to be one greater than what we just found:

````
>>> word.find('n', 3)
4
````

I can see this is correct:

````
>>> word[4]
'n'
````

And can update `guessed` again:

````
>>> guessed[4] = 'n'
>>> guessed
['_', '_', 'n', '_', 'n', '_']
````

When I call `word.find` next, I'll get `-1` to indicate the character is not found:

````
>>> word.find('n', 5)
-1
````

Contrast this with `str.index` to see that it creates an exception which is why we use `find`:

````
>>> word.index('n', 5)
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
ValueError: substring not found
````

If all the previous checks failed, then the `new_guess` was not found in the `word`, so I increment the `num_misses` and let the user know.

Finally, I call `play` again, passing it the new `state` as a new `dict`. Anytime a `return` statement is called, the recursion stops and execution returns to the first place I called `play`. Using the final `return` value which should be a `bool`, I can decide whether to print "You win!" or "You lose, loser!"

## Testing the play

I can test my `play` with a function:

````
>>> from hangman import play
>>> def test_play():
...     assert play({'word': 'banana', 'inputs': list('abn')}) == True
...     assert play({'word': 'banana', 'inputs': list('abcdefghijklm')}) == False
...     assert play({'word': 'banana', 'inputs': list('???')}) == True
...     assert play({'word': 'banana', 'inputs': list('!')}) == False
...
>>> test_play()
...
````

## Further

Here are some changes you could make to your program:

* Read a wordlist that has punctuation and use only a unique list for your words
* Add a limit to the number of hints the user can request with `?`
* Add a random insult every time the user asks for a hint
* Add a `quiet` flag to keep `play` from executing any `print` statements