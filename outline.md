# Playful Python Outline

I aim to have 40-50 programs complete with specs, examples, inputs, and test suites. They won't necessarily have a specific order, but they will be grouped into easiest/harder/hardest categories. As many programs use common ideas (e.g., regular expressions, graphs, infinite loops), there will be an appendix section with explanations of how to explore those ideas. 

I have in mind a layout where each program gets four pages:

        1        2               3        4
    +--------+--------+      +--------+--------+
    |        |        |      |        |        |
    |        |        |      |        |        |
    |        |        |      |        |        |
    | illus/ | specs  |      |solution| notes  |
    | info   |        |      |        |        |
    |        |        |      |        |        |
    |        |        |      |        |        |
    +--------+--------+      +--------+--------+

1. If a short program, perhaps an illustration; if longer, maybe some background or hints.
2. The `README.md` information (specs, example output)
3. The `solution.py` contents
4. Annotation of the solution with comments on lines, sections

# Programs

> "The only way to learn a new programming language is by writing programs in it." - Dennis Ritchie

The goal is to get the reader to become a *writer* -- to try to solve the problems. One technique in teaching is to first present a problem without showing how to solve it. Once the student engages with the problem, they find they want and need the object of the lesson. Each program is intended to flex some programming technique or idea like playing with lists or contemplating regular expressions or using dictionaries. By using `argparse` for the programs, we also cover validation of user input.

## Easiest

* **howler**: Uppercase input text so they YELL AT YOU LIKE "HOWLER" MESSAGES IN HARRY POTTER. (Could also be called "OWEN MEANY"?)
* **jump_the_five**: Numeric encryption based on "The Wire."
* **bottles_of_beer**: Produce the "Bottle of Beer on the Wall" song. Explores the basic idea of an algorithm and challenges the programmer to format strings.
* **picnic**: Write the picnic game. Uses input, lists.
* **apples_and_bananas**: Substitute vowels in text, e.g., "bananas" -> "bononos". While the concept is substitution of characters in a string which is actually trivial, it turns out there are many (at least 7) decent ways to accomplish this task!
* **gashlycrumb**: Create a morbid lookup table from text. Naturual use of dictionaries.
* **movie_reader**: Print text character-by-character with pauses like in the movies. How to read text by character, use STDOUT/flush, and pause the program.
* **palindromes**: Find palindromes in text. Reading input, manipulation of strings.
* **ransom_note**: Transform input text into "RaNSom cASe". Manipulation of text.
* **rhymer**: Produce rhyming "words" from input text. 
* **rock_paper_scissors**: Write Rock, Paper, Scissors game. Infinite loops, dictionaries.

## Harder

* **abuse**: Generate insults from lists of adjectives and nouns. Use of randomness, sampling, and lists.
* **bacronym**: Retrofit words onto acronyms. Use of randomness and dictionaries.
* **blackjack**: Play Blackjack (card game). Use of randomness, combinations, dictionaries.
* **family_tree**: Use GraphViz to visualize a family tree from text. Parsing text, creating graph structures, creating visual output.
* **gematria**: Calculate numeric values of words from characters. Manipulation of text, use of higher-order functions.
* **guess**: Write a number-guessing game. Use of randomness, validation/coercion of inputs, use of exceptions.
* **kentucky_fryer**: Turn text into Southern American English. Parsing, manipulation of text.
* **mad_libs**: TBD
* **markov_words**: Markov chain to generate words. Use of n-grams/k-mers, graphs, randomness, logging.
* **piggie**: Encode text in Pig Latin. Use of regular expressions, text manipulation.
* **sound**: Use Soundex to find rhyming words from a word list.
* **substring**: Write a game to guess words sharing a common substring. Dictionaries, k-mers/n-grams.
* **tictactoe**: Write a Tic-Tac-Toe game. Randomness, state.
* **twelve_days_of_christmas**: Produce the "12 Days of Christmas" song. Algorihtms, loops.
* **war**: Play the War card game. Combinations, randomness.

## Hardest

* **anagram**: Find anagrams of text. Combinations, permutations, dictionaries.
* **hangman**: Write a Hangman (word/letter-guessing game). Randomness, game state, infinite loops, user input, validation.
* **markov_chain**: Markov chain to generate text. N-grams at word level, parsing text, list manipulations.
* **morse**: Write a Morse encoder/decoder. Dictionaries, text manipulation.
* **rot13**: ROT13-encode input text. Lists, encryption.
