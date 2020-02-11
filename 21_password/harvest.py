#!/usr/bin/env python3
"""
Author : Ken Youens-Clark <kyclark@gmail.com>
Date   : 2019-11-23
Purpose: Harvest parts of speech from texts
"""

import argparse
import os
import spacy
from collections import Counter


# --------------------------------------------------
def get_args():
    """Get command-line arguments"""

    parser = argparse.ArgumentParser(
        description='Harvest parts of speech from texts',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    parser.add_argument('file',
                        metavar='FILE',
                        type=argparse.FileType('r'),
                        nargs='+',
                        help='Input file(s)')

    parser.add_argument('-o',
                        '--outdir',
                        help='Output directory',
                        metavar='str',
                        type=str,
                        default='words')

    parser.add_argument('-l',
                        '--limit',
                        metavar='int',
                        type=int,
                        default=0,
                        help='Limit to this many')

    return parser.parse_args()


# --------------------------------------------------
def main():
    """Make a jazz noise here"""

    args = get_args()
    out_dir = args.outdir

    if not os.path.isdir(out_dir):
        os.makedirs(out_dir)

    # Load English tokenizer, tagger, parser, NER and word vectors
    nlp = spacy.load("en_core_web_sm")

    nouns, adjs, verbs = Counter(), Counter(), Counter()
    for fh in args.file:
        doc = nlp(fh.read())

        for token in doc:
            pos, word = token.pos_, token.lemma_.lower()

            if pos == 'NOUN':
                nouns.update([word])
            elif pos == 'VERB':
                verbs.update([word])
            elif pos == 'ADJ':
                adjs.update([word])

    def limiter(words):
        return sorted(list(map(lambda t: t[0], words.most_common(
            args.limit)))) if args.limit else sorted(words)

    def write(words, name):
        if words:
            out_fh = open(os.path.join(out_dir, name), 'wt')
            out_fh.write('\n'.join(limiter(words)) + '\n')

    write(verbs, 'verbs.txt')
    write(nouns, 'nouns.txt')
    write(adjs, 'adjs.txt')

    print(f'Done, see output in "{out_dir}".')


# --------------------------------------------------
if __name__ == '__main__':
    main()
