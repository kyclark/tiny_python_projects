# Hangman

Write a Python program called `hangman.py` that will play a game of Hangman which is a bit like "Wheel of Fortune" where you present the user with a number of elements indicating the length of a word. For our game, use the underscore `_` to indicate a letter that has not been guessed. The program should take `-n|--minlen` minimum length (default `5`) and `-l|--maxlen` maximum length options (default `10`) to indicate the minimum and maximum lengths of the randomly chosen word taken from the `-w|--wordlist` option (default `/usr/share/dict/words`). It also needs to take `-s|--seed` to for the random seed and the `-m|--misses` number of misses to allow the player.

The game is intended to be interactive, but I want you to additionally take an `-i|--inputs` option that is a string of letters to use as guesses so that we can write a test.

When run with the `-h|--help` flags, it should present a usage statement:

````
$ ./hangman.py -h
usage: hangman.py [-h] [-l MAXLEN] [-n MINLEN] [-m MISSES] [-s SEED]
                  [-w WORDLIST] [-i INPUTS]

Hangman

optional arguments:
  -h, --help            show this help message and exit
  -l MAXLEN, --maxlen MAXLEN
                        Max word length (default: 10)
  -n MINLEN, --minlen MINLEN
                        Min word length (default: 5)
  -m MISSES, --misses MISSES
                        Max number of misses (default: 10)
  -s SEED, --seed SEED  Random seed (default: None)
  -w WORDLIST, --wordlist WORDLIST
                        Word list (default: /usr/share/dict/words)
  -i INPUTS, --inputs INPUTS
                        Input choices (default: )
````

If given a bad `--wordlist`, error out (print the problem and exit with a non-zero status) with a message like so:

````
$ ./hangman.py -w kdfkj
usage: hangman.py [-h] [-l MAXLEN] [-n MINLEN] [-m MISSES] [-s SEED]
                  [-w WORDLIST] [-i INPUTS]
hangman.py: error: argument -w/--wordlist: can't open 'kdfkj': [Errno 2] \
No such file or directory: 'kdfkj'
````

If given a value less than 1 for `--minlen`, error out:

````
$ ./hangman.py -n -4
usage: hangman.py [-h] [-l MAXLEN] [-n MINLEN] [-m MISSES] [-s SEED]
                  [-w WORDLIST] [-i INPUTS]
hangman.py: error: --minlen "-4" must be positive
````

If given a `--maxlen` value greater than 20, error out:

````
$ ./hangman.py -l 30
usage: hangman.py [-h] [-l MAXLEN] [-n MINLEN] [-m MISSES] [-s SEED]
                  [-w WORDLIST] [-i INPUTS]
hangman.py: error: --maxlen "30" must be < 20
````

Error out if the `--minlen` is greater than the `--maxlen`:

````
$ ./hangman.py -l 5 -n 10
usage: hangman.py [-h] [-l MAXLEN] [-n MINLEN] [-m MISSES] [-s SEED]
                  [-w WORDLIST] [-i INPUTS]
hangman.py: error: --minlen "10" is greater than --maxlen "5"
````

To play, you will initiate an inifinite loop and keep track of the game state, e.g., the word to guess, the letters already guessed, the letters found, the number of misses. As this is an interactive game, you will normally use the `input` function to get a letter from the user. If given `--inputs`, bypass the `input` prompt and instead use those letters in turn.

If the user guesses a letter that is in the word, replace the `_` characters with the letter. If the user guesses the same letter twice, admonish them. If the user guesses a letter that is not in the word, increment the misses and let them know they missed. If the user guesses too many times, exit the game and insult them. If they correctly guess the word, let them know and exit the game.

````
$ ./hangman.py -s 2
_ _ _ _ _ _ _ (Misses: 0)
Your guess? ("?" for hint, "!" to quit) a
There is no "a"
_ _ _ _ _ _ _ (Misses: 1)
Your guess? ("?" for hint, "!" to quit) i
There is no "i"
_ _ _ _ _ _ _ (Misses: 2)
Your guess? ("?" for hint, "!" to quit) e
_ _ _ _ _ _ e (Misses: 2)
Your guess? ("?" for hint, "!" to quit) o
o _ o _ _ _ e (Misses: 2)
Your guess? ("?" for hint, "!" to quit) z
o z o _ _ _ e (Misses: 2)
Your guess? ("?" for hint, "!" to quit) t
o z o t _ _ e (Misses: 2)
Your guess? ("?" for hint, "!" to quit) p
o z o t _ p e (Misses: 2)
Your guess? ("?" for hint, "!" to quit) y
You win. You guessed "ozotype" with "2" misses!
````

Play the `solution.py` a few times to get a feel for how the game should work.

Hints:

* Leverage `get_args` and `argparse` to validate inputs. Use `type=argparse.FileType('r')` for the `--wordlist`. Check the value of `--minlen` and `--maxlen` inside `get_args` and use `parser.error` to error out.