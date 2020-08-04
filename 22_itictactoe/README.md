# Interactive Tic-Tac-Toe 

https://www.youtube.com/playlist?list=PLhOuww6rJJNOlaMDHHIQrvWZn--GGNlHU

Write a Python program called `itictactoe.py` that will play an interactive game of Tic-Tac-Toe starting from a blank board and iterating between players `X` and `O` until the game is finished due to a draw or a win.
When the game starts, a blank board with cells 1-9 should be shown along with a prompt for the current player (always starting with `X`) to select a cell:

```
-------------
| 1 | 2 | 3 |
-------------
| 4 | 5 | 6 |
-------------
| 7 | 8 | 9 |
-------------
Player X, what is your move? [q to quit]: 1
```

If a player tries to select an occupied cell, the move is disallowed and the same player goes until a valid choice is made:

```
-------------
| X | 2 | 3 |
-------------
| 4 | 5 | 6 |
-------------
| 7 | 8 | 9 |
-------------
Player O, what is your move? [q to quit]: 1
-------------
| X | 2 | 3 |
-------------
| 4 | 5 | 6 |
-------------
| 7 | 8 | 9 |
-------------
Cell "1" already taken
Player O, what is your move? [q to quit]:
```

Play should stop when a player has won:

```
-------------
| X | O | 3 |
-------------
| X | O | 6 |
-------------
| 7 | 8 | 9 |
-------------
Player X, what is your move? [q to quit]: 7
X has won!
```

Or when the game is a draw:

```
-------------
| X | O | O |
-------------
| O | X | X |
-------------
| X | 8 | O |
-------------
Player X, what is your move? [q to quit]: 8
All right, we'll call it a draw.
```
