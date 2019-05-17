#!/usr/bin/env python3
"""
Author : Ken Youens-Clark <kyclark@gmail.com>
Date   : 2019-02-06
Purpose: Rock the Casbah
"""

import os
import re
import sys


# --------------------------------------------------
def main():
    args = sys.argv[1:]

    if len(args) != 1:
        print('Usage: {} STATE'.format(os.path.basename(sys.argv[0])))
        sys.exit(1)

    state = args[0]

    if not re.search('^[.XO]{9}$', state):
        print(
            'State "{}" must be 9 characters of only ., X, O'.format(state),
            file=sys.stderr)
        sys.exit(1)

    winning = [[0, 1, 2], [3, 4, 5], [6, 7, 8], [0, 3, 6], [1, 4, 7],
               [2, 5, 8], [0, 4, 8], [2, 4, 6]]

    winner = 'No winner'

    # for player in ['X', 'O']:
    #     for combo in winning:
    #         i, j, k = combo
    #         if state[i] == player and state[j] == player and state[k] == player:
    #             winner = player
    #             break

    # for player in ['X', 'O']:
    #     for combo in winning:
    #         chars = []
    #         for i in combo:
    #             chars.append(state[i])

    #         if ''.join(chars) == player * 3:
    #             winner = player
    #             break

    # for player in ['X', 'O']:
    #     for i, j, k in winning:
    #         chars = ''.join([state[i], state[j], state[k]])
    #         if ''.join(chars) == '{}{}{}'.format(player, player, player):
    #             winner = player
    #             break

    for player in ['X', 'O']:
        for i, j, k in winning:
            combo = [state[i], state[j], state[k]]
            if combo == [player, player, player]:
                winner = '{} has won'.format(player)
                break

    # for combo in winning:
    #     group = list(map(lambda i: state[i], combo))
    #     for player in ['X', 'O']:
    #         if all(x == player for x in group):
    #             winner = player
    #             break

    print(winner)


# --------------------------------------------------
main()
