#!/usr/bin/env python3
""" Demonstrating type hints """

from typing import List, NamedTuple, Optional


class State(NamedTuple):
    board: List[str]
    player: str
    quit: bool
    draw: bool
    error: Optional[str]
    winner: Optional[str]


state = State(board='.' * 9,
              player='X',
              quit='False',
              draw=False,
              error=None,
              winner=None)

print(state)
