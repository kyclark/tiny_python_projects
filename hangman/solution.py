#!/usr/bin/env python3
"""Hangman game"""

import argparse
import io
import random
import re
import sys


# --------------------------------------------------
def get_args():
    """parse arguments"""

    parser = argparse.ArgumentParser(
        description='Hangman',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    parser.add_argument('-l',
                        '--maxlen',
                        help='Max word length',
                        type=int,
                        default=10)

    parser.add_argument('-n',
                        '--minlen',
                        help='Min word length',
                        type=int,
                        default=5)

    parser.add_argument('-m',
                        '--misses',
                        help='Max number of misses',
                        type=int,
                        default=10)

    parser.add_argument('-s',
                        '--seed',
                        help='Random seed',
                        type=str,
                        default=None)

    parser.add_argument('-w',
                        '--wordlist',
                        help='Word list',
                        type=argparse.FileType('r'),
                        default='/usr/share/dict/words')

    parser.add_argument('-i',
                        '--inputs',
                        help='Input choices',
                        type=str,
                        default='')

    args = parser.parse_args()

    if args.minlen < 1:
        parser.error('--minlen "{}" must be positive'.format(args.minlen))

    if args.maxlen > 20:
        parser.error('--maxlen "{}" must be < 20'.format(args.maxlen))

    if args.minlen > args.maxlen:
        parser.error('--minlen "{}" is greater than --maxlen "{}"'.format(
            args.minlen, args.maxlen))

    return args


# --------------------------------------------------
def get_words(wordlist, min_len, max_len):
    """Read wordlist (file handle), return words in range(min_len, max_len)"""

    good = '^[a-z]{' + str(min_len) + ',' + str(max_len) + '}$'
    is_good = lambda w: re.match(good, w)
    return list(filter(is_good, wordlist.read().lower().split()))


# --------------------------------------------------
def test_get_words():
    """Test get_words"""

    text = 'Apple banana COW da epinephrine'
    assert get_words(io.StringIO(text), 1, 20) == text.lower().split()
    assert get_words(io.StringIO(text), 5, 10) == ['apple', 'banana']
    assert get_words(io.StringIO(text), 3, 10) == ['apple', 'banana', 'cow']


# --------------------------------------------------
def main():
    """main"""

    args = get_args()
    words = get_words(args.wordlist, args.minlen, args.maxlen)
    random.seed(args.seed)
    result = play({
        'word': random.choice(words),
        'max_misses': args.misses,
        'inputs': list(args.inputs),
    })

    print('You win!' if result else 'You lose, loser!')


# --------------------------------------------------
def play(state):
    """Play a round given a `dict` of the current state of the game"""

    word = state.get('word')
    if not word:
        print('No word!')
        return False

    guessed = state.get('guessed', list('_' * len(word)))
    prev_guesses = state.get('prev_guesses', set())
    num_misses = state.get('num_misses', 0)
    max_misses = state.get('max_misses', 10)
    inputs = state.get('inputs', [])

    if ''.join(guessed) == word:
        msg = 'You guessed "{}" with "{}" miss{}.'
        print(msg.format(word, num_misses, '' if num_misses == 1 else 'es'))
        return True

    if num_misses >= max_misses:
        print('The word was "{}."'.format(word))
        return False

    print('{} (Misses: {})'.format(' '.join(guessed), num_misses))

    get_char = lambda: input('Your guess? ("?" for hint, "!" to quit) ').lower()
    new_guess = inputs.pop(0) if inputs else get_char()

    if new_guess == '!':
        print('Better luck next time.')
        return False
    elif new_guess == '?':
        new_guess = random.choice([c for c in word if c not in guessed])
        num_misses += 1

    if not re.match('^[a-z]$', new_guess):
        print('"{}" is not a letter.'.format(new_guess))
        num_misses += 1
    elif new_guess in prev_guesses:
        print('You already guessed that.')
    elif new_guess in word:
        prev_guesses.add(new_guess)
        last_pos = 0
        while True:
            pos = word.find(new_guess, last_pos)
            if pos < 0:
                break
            elif pos >= 0:
                guessed[pos] = new_guess
                last_pos = pos + 1
    else:
        print('There is no "{}."'.format(new_guess))
        num_misses += 1

    return play({
        'word': word,
        'guessed': guessed,
        'num_misses': num_misses,
        'prev_guesses': prev_guesses,
        'max_misses': max_misses,
        'inputs': inputs,
    })


# --------------------------------------------------
def test_play():
    """Test play"""

    assert play({'word': 'banana', 'inputs': list('abn')}) == True
    assert play({'word': 'banana', 'inputs': list('abcdefghijklm')}) == False
    assert play({'word': 'banana', 'inputs': list('???')}) == True
    assert play({'word': 'banana', 'inputs': list('!')}) == False


# --------------------------------------------------
if __name__ == '__main__':
    main()
