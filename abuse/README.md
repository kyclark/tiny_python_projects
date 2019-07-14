# Dial-A-Curse

Write a Python program called `abuse.py` that generates some `-n|--number` of insults (default `3`) by randomly combining some number of `-a|--adjectives` (default `2`) with a noun (see below). Be sure your program accepts a `-s|--seed` argument (default `None`) to pass to `random.seed`.

The are the adjectives you should use:

bankrupt base caterwauling corrupt cullionly detestable dishonest
false filthsome filthy foolish foul gross heedless indistinguishable
infected insatiate irksome lascivious lecherous loathsome lubbery old
peevish rascaly rotten ruinous scurilous scurvy slanderous
sodden-witted thin-faced toad-spotted unmannered vile wall-eyed

And these are the nouns:

Judas Satan ape ass barbermonger beggar block boy braggart butt
carbuncle coward coxcomb cur dandy degenerate fiend fishmonger fool
gull harpy jack jolthead knave liar lunatic maw milksop minion
ratcatcher recreant rogue scold slave swine traitor varlet villain worm

If run with the `-h|--help` flag, the program should generate usage:

````
$ ./abuse.py -h
usage: abuse.py [-h] [-a int] [-n int] [-s int]

Argparse Python script

optional arguments:
  -h, --help            show this help message and exit
  -a int, --adjectives int
                        Number of adjectives (default: 2)
  -n int, --number int  Number of insults (default: 3)
  -s int, --seed int    Random seed (default: None)
````

When run with no arguments, the program should generate insults using the defaults:
  
````  
$ ./abuse.py
You slanderous, rotten block!
You lubbery, scurilous ratcatcher!
You rotten, foul liar!
````

It's unlikely you'll get the same output above when you run yours because no seed was set. The following, however, should be exactly reproducible due to the `--seed`:

````
$ ./abuse.py -s 1 -n 2 -a 1
You rotten rogue!
You lascivious ape!
$ ./abuse.py -s 2 -n 4 -a 4
You scurilous, foolish, vile, foul milksop!
You cullionly, lubbery, heedless, filthy lunatic!
You foul, lecherous, infected, slanderous degenerate!
You base, ruinous, slanderous, false liar!
````

If run with a `--number` less than 1, exit with an error code and message, preferably with the usage:

````
$ ./abuse.py -n -4
usage: abuse.py [-h] [-a int] [-n int] [-s int]
abuse.py: error: --number "-4" cannot be less than 1
````

Hints:

* You can use three single or double quotes (\"\"\") to create a multi-line string and then `split()` that to get a list of strings. This is easier than individually quoting a long list of shorter strings (e.g., the list of adjectives and nouns).
* Perform the check for `--number` inside the `get_args` function and use `parser.error` to throw the error while printing a message and the usage.
* If you set the default for `args.seed` to `None` while using a `type=int`, you should be able to directly pass the argument's value to `random.seed` to control testing.
* Use a `for` loop with the `range` function to create a loop that will execute `--number` of times to generate each insult.
* Look at the `sample` and `choice` functions in the `random` module for help in selecting some adjectives and a noun.
* To construct an insult string to print, you can use the `+` operator to concatenate strings, use the `str.join` method, or use format strings (and maybe other methods?).
