The only argument to the program is a single positional `file` which I chose to define with `type=argparse.FileType('r')` on line 17 to save me the trouble of testing for a file though you could test yourself and will pass the test as long as your error message includes `No such file or directory: '{}'` for the given file.

### Reading the puzzle input

I chose to define a few additional functions while keeping most of the programs logic in the `main`. The first is `read_puzzle` that reads the file given by the user. As noted in the README, this file has the puzzle grid, an empty line, and then the list of words to search, so I define `read_puzzle` to accept the file (`fh`) as an argument and return two lists that represent the `puzzle` and `words` (line 28). 

There list of `words` is really most naturally represented as a `list` of `str` elements, but the `puzzle` is a bit more complicated. After working through a couple of solutions, I decided I would number all the characters in the grid in order to know which ones to reveal at the end and which ones to replace with a period, so I define a `cell` variable initialized to `0` to keep count of the characters. 

Here is my mental model of the puzzle:

	Puzzle			          Model
			 		  Col 0   Col 1   Col 2
	A B C	    Row	0 (A, 1)  (B, 2)  (C, 3)
	D E F       Row 1 (D, 4)  (E, 5)  (F, 6)
	G H I		Row 2 (G, 7)  (H, 8)  (I, 9)

Lastly, I need to know if I'm reading the first part of the file with the puzzle or the latter part with the words, so I define a `read` variable initialized to `'puzzle'` on line 30.

I start reading with `for line in` the file, but I want to chop off the trailing whitespace so I `map(str.rstrip, fh)`. Remember not to include parens `()` on `str.rstrip` as we want to *reference* the function not *call* it. The first operation in the loop is to check for an empty string (`''`, because we remove the newlines). If we find that, then we note the switch to reading the `'words'` and use `continue` to skip to the next iteration of the loop. 

If I'm reading the puzzle part of the file. then I want to read each character (line 38), increment the `cell` counter, then create a new tuple with the character and it's cell number, appending this to the `row`, a list to hold all the new tuples. The `row` then gets appended to the `puzzle` list that will eventually be a `list` of rows, each of which is a `list` of tuples representing `(char, cell)`. 

If we get to line 44, we must be reading the latter part of the file, so the `line` is actually a word that I will `append` to the `words` list. Before doing that, however, I will `replace` any space (`' '`) with the empty string (`''`) so as to remove spaces (cf. the `ice_cream.txt` input). Finally I `return puzzle, words` which is actually returning a tuple created by the comma `,` and which I immediately unpack on line 124.

### Finding all the strings

I always try to make a function fit into about 50 lines of code.  While my `read_puzzle` fits into 22 lines, the other function, `all_combos` is considerable longer. I couldn't find a way to shorten it, so I at least try to keep the idea fully contained to one function that, once it works, I no longer need to consider. The idea of this function is to find all the strings possible by reading each row, column, and diagonal both forward and backward. To do this, I first figure out how many rows and columns are present by checking the length (`len`) of the `puzzle` itself (the number of rows) and the length of the first row (the number of character in the first row). I double-check on line 56 that `all` of the the rows have the same `len` as the first one, using the `die` function from the `dire` module to print a message to STDERR and then `sys.exit(1)` to indicate a failure.

The `all_combos` will return a `list` of the characters and their cells, so I define `combos` on line 59 as an empty list (`[]`). Reading the rows is easiest on lines 61-62 as we just copy each `row` into `combo`. Reading the columns is done by moving from column `0` to the last column using the `range(num_cols)` (remembering the last number is not included which is important because if there are 10 columns then we need to move from column `0` to column `9`). I can then extract each column position from each row in the puzzle by indexing `puzzle[row_num][col_num]` and appending those to the `combos`.

The diagonals are the trickiest. I chose to go up (lower-left to upper-right) first. I start in the top-left corner, row `0` and column `0`. For each row, I'm going to move diagonally upwards (toward the top of the grid) which is actually counting *down* from the row I'm on, so I actually need to move `row_i` *up* and then `row_j` *down*. (I use `i` for "integer" and then `j` because "j" comes after "i". This is a typical naming convention. If I needed a third counter, I'd move to `k`.) I count `row_j` *down* by using `range(row_i, -1, -1)` (where the first `-1` is so I can count all the way to `0` and the second indicates the step should go down by one), I need to move the `col_num` over by `1`. If I successfully read a diagonal, I append that to the `combos`. 

The next block starts at the bottommost row of the and moves across the columns and is very similar to how I read the columns. Then moving into reading the diagonals in a downward (upper-left to bottom-right) fashion, I modified the other two blocks to handle the specifics. Finally at the end of the function (line 120), I want to `extend` the `combos` list by adding a `reversed` version of each combo. It's necessary to coerce `list(reversed(c))` otherwise we'd end up with references to `reversed` *objects*. 

### Solving the puzzle

Once we've read the puzzle and found all the possible strings both forwards and backwards, we can then look for each of the words in each of the strings. In my `main`, I want to use sets to note all the words that are `found` as well as the cell numbers to `reveal`. Because I'll be reading lists of tuples where the character is in the first position and the cell number in the second, I define two functions `fst` and `snd` (stolen from Haskell) that I can use in `map` expressions. I iterate `for word in words` (line 146) and `for combo in combos` to check all combinations. Recall that the `combo` is a list of tuples:

````
>>> combo = [('X', 1), ('F', 2), ('O', 3), ('O', 4)]
````

so I can build a string from the characters in the `fst` position of the tuples by mapping them to `fst`:

````
>>> list(map(fst, combo))
['X', 'F', 'O', 'O']
````

and joining them on an empty string:

````
>>> test = ''.join(map(fst, combo))
>>> test
'XFOO'
````

Then I check if the `word` is in the `test` string:

````
>>> word='FOO'
>>> word in test
True
````

If it is, then I can find where it starts with the `str.index` function:

````
>>> start = test.index(word)
>>> start
1
````

I know then end is:

````
>>> end = start + len(word)
>>> end
4
````

I can use that information to iterate over the elements in the `combo` to extract the cell numbers which are in the `snd` position of the tuple because ultimately what I need to print is the original puzzle grid with the cells showing the hidden words and all the others masked. I can extract a list slice using `combo[start:end]`, `map` those elements through `snd` to get the `cell` and `add` those to the `reveal` set. I can also note that I `found` the `word`.

At line 157, I start the work of printing the revealed puzzle, iterating over the original rows in the puzzle and over each cell in the row. If the cell number is in the `reveal` set, I chose the character (in the first position of the tuple); otherwise I use a period (`.`). Finally I note any missing words by looking to see if any of the original words were not in the `found` set.
