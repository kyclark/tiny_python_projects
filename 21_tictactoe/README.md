# Tic-Tac-Toe

https://www.youtube.com/playlist?list=PLhOuww6rJJNObtig0Kr-jgTJly1x04jgz

Create a Python program called `tictactoe.py` that will play a single round of the game Tic-Tac-Toe.
The program should accept the following parameters:

* `-b`|`--board`: The optional state of the board for the play. This will be a string of 9 characters representing the 9 cells of the 3x3 board. The string should be composed only of `X` and `O` to denote a player occupying that cell or `.` to show that the cell is open. The default is 9 '.' as all cells are open.
* `-p`|`--player`: An optional player which must be either `X` or `O`.
* `-c`|`--cell`: An optional cell which must be in the range 1-9 (inclusive).

Here is the usage the program should print for `-h` or `--help`:

```
$ ./tictactoe.py -h
usage: tictactoe.py [-h] [-b str] [-p str] [-c int]

Tic-Tac-Toe

optional arguments:
  -h, --help            show this help message and exit
  -b str, --board str   The state of the board (default: .........)
  -p str, --player str  Player (default: None)
  -c int, --cell int    Cell 1-9 (default: None)
```

The program will print the state of the board plus any modifications to the state made by `--player` and `--cell` along with the final outcome of the game which can either be "No winner" or "{player} has won."

When run with no arguments, it should print a blank Tic-Tac-Toe board and "No winner":

```
$ ./tictactoe.py
-------------
| 1 | 2 | 3 |
-------------
| 4 | 5 | 6 |
-------------
| 7 | 8 | 9 |
-------------
No winner.
```

Given a valid `--player` trying to take an unoccupied `--cell`, the program should modify the state before printing the board and deciding the outcome:

```
$ ./tictactoe.py -p X -c 1
-------------
| X | 2 | 3 |
-------------
| 4 | 5 | 6 |
-------------
| 7 | 8 | 9 |
-------------
No winner.
```

The program should error out for a bad `--board`:

```
$ ./tictactoe.py -b ABC......
usage: tictactoe.py [-h] [-b str] [-p str] [-c int]
tictactoe.py: error: --board "ABC......" must be 9 characters of ., X, O
```

Or a bad `--cell`:

```
$ ./tictactoe.py -p X -c 10
usage: tictactoe.py [-h] [-b str] [-p str] [-c int]
tictactoe.py: error: argument -c/--cell: invalid choice: 10 \
(choose from 1, 2, 3, 4, 5, 6, 7, 8, 9)
```

Or a bad `--player`:

```
$ ./tictactoe.py -p A -c 1
usage: tictactoe.py [-h] [-b str] [-p str] [-c int]
tictactoe.py: error: argument -p/--player: invalid choice: 'A' \
(choose from 'X', 'O')
```

Or in the event a `--player` is trying to take an occupied `--cell`:

```
$ ./tictactoe.py -b X........ -p O -c 1
usage: tictactoe.py [-h] [-b str] [-p str] [-c int]
tictactoe.py: error: --cell "1" already taken
```

Or if only `--player` or `--cell` is provided:

```
$ ./tictactoe.py --player X
usage: tictactoe.py [-h] [-b board] [-p player] [-c cell]
tictactoe.py: error: Must provide both --player and --cell
```

The program should detect a winning state:

```
$ ./tictactoe.py -b .XX....OO -p X -c 1
-------------
| X | X | X |
-------------
| 4 | 5 | 6 |
-------------
| 7 | O | O |
-------------
X has won!
```

The program should pass all tests:

```
$ make test
pytest -xv test.py
============================= test session starts ==============================
...
collected 15 items

test.py::test_exists PASSED                                              [  6%]
test.py::test_usage PASSED                                               [ 13%]
test.py::test_no_input PASSED                                            [ 20%]
test.py::test_bad_board PASSED                                           [ 26%]
test.py::test_bad_player PASSED                                          [ 33%]
test.py::test_bad_cell_int PASSED                                        [ 40%]
test.py::test_bad_cell_str PASSED                                        [ 46%]
test.py::test_both_player_and_cell PASSED                                [ 53%]
test.py::test_good_board_01 PASSED                                       [ 60%]
test.py::test_good_board_02 PASSED                                       [ 66%]
test.py::test_mutate_board_01 PASSED                                     [ 73%]
test.py::test_mutate_board_02 PASSED                                     [ 80%]
test.py::test_mutate_cell_taken PASSED                                   [ 86%]
test.py::test_winning PASSED                                             [ 93%]
test.py::test_losing PASSED                                              [100%]

============================== 15 passed in 2.12s ==============================
```
