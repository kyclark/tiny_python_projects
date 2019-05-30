# Tic-Tac-Toe Outcome

Create a Python program called `outcome.py` that takes a given Tic-Tac-Toe state as it's only (positional) argument and reports if X or O has won or if there is no winner. The state should only contain the characters ".", "O", and "X", and must be exactly 9 characters long. If there is not exactly one argument, print a "usage" statement.

````
$ ./outcome.py
Usage: outcome.py STATE
$ ./outcome.py ..X.OA..X
State "..X.OA..X" must be 9 characters of only ., X, O
$ ./outcome.py ..X.OX...
No winner
$ ./outcome.py ..X.OX..X
X has won
````
