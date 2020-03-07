#!/usr/bin/env python3
""" Demonstrating type hints """

from typing import List, NamedTuple, Optional


class State(NamedTuple):
    board: List[str] = list('.' * 9)
    player: str = 'X'
    quit: bool = False
    draw: bool = False
    error: Optional[str] = None
    winner: Optional[str] = None


state = State(quit='False')

print(state)
