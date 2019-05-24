# Markov Chain

Write a Python program called `markov.py` that takes one or more text files as positional arguments for training. Use the `-n|--num_words` argument (default `2`) to find clusters of words and the words that follow them, e.g., in "The Bustle" by Emily Dickinson:

    The bustle in a house
    The morning after death
    Is solemnest of industries
    Enacted upon earth,—

    The sweeping up the heart,
    And putting love away
    We shall not want to use again
    Until eternity.

If `n=1`, then we find that "The" can be followed by "bustle," "morning," and "sweeping. There is a "the" followed by "heart," but we're not going to alter the text in any way, including removing punctuation, so just use `str.split` on the text to break up the words. 

To begin your text, choose a random word (or words) that begin with an uppercase letter. Then randomly select the next word in the chain, keep track of the floating window of the `-n` words, and keep selecting the next words until you have matched or exceeded the `-l|--length` argument of the number of characters (default 500) to emit at which point you should stop when you find a word that terminates with `.`, `!`, or `?`.

If you use `str.split` to get the words from the training text, you'll be removing any newlines from the text, so use a `-w|--text_width` argument (default 70) to introduce newlines in the output before the text exceeds that number of characters on the line.

Because of the use of randomness, you should include a `-s|--seed` argument (default `None`) to pass to `random.seed`.

Occassionally you may chose a path that terminates. That is, in selecting the next word, you may find there is no next-next word. In that case, just exit the program.

My implementation includes a `-d|--debug` option that will write a `.log` file so you can inspect my data structures and logic as you write your own version.

You should find many diverse texts and use them all as training files with varying numbers for `-n` to see how the texts will be mixed. The results are endlessly entertaining.

# Background

Read about Markov chains at https://en.wikipedia.org/wiki/Markov_chain or in _The Practice of Programming_ by Brian Kernighan and Rob Pike where they discuss implementations in C, C++, Java, awk, and Perl. 

````
$ ./markov.py
usage: markov.py [-h] [-l int] [-n int] [-s int] [-w int] [-d] FILE [FILE ...]
markov.py: error: the following arguments are required: FILE
$ ./markov.py -h
usage: markov.py [-h] [-l int] [-n int] [-s int] [-w int] [-d] FILE [FILE ...]

Markov Chain

positional arguments:
  FILE                  Training file(s)

optional arguments:
  -h, --help            show this help message and exit
  -l int, --length int  Output length (characters) (default: 500)
  -n int, --num_words int
                        Number of words (default: 2)
  -s int, --seed int    Random seed (default: None)
  -w int, --text_width int
                        Max number of characters per line (default: 70)
  -d, --debug           Debug to ".log" (default: False)
$ ./markov.py ../inputs/const.txt
Discoveries; To constitute Tribunals inferior to the seat of the
Senate and House of Representatives shall have been committed, which
district shall have the Qualifications requisite for Electors of the
sixth Year, so that one third may be imposed on such Importation, not
exceeding three on the Journal. Neither House, during the Time of
Adjournment, he may require it. No Bill of Attainder or ex post facto
Law shall be established by Law: but the Party convicted shall
nevertheless be liable and subject to their Consideration such
Measures as he shall nominate, and by and with the Advice and Consent
of the government of the United States under this Constitution, or,
on the List the said Office, the same State claiming Lands under
Grants of different States; between Citizens of each shall constitute
a Quorum to do Business; but a smaller number may adjourn from day to
day, and may be included within this Union, according to their
Consideration such Measures as he shall nominate, and by and with the
Advice and Consent of the United States.
````
