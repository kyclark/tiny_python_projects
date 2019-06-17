#!/usr/bin/env bash

set -u

OUT_DIR="test-outs"
[[ ! -d "$OUT_DIR" ]] && mkdir -p "$OUT_DIR"

./markov.py ../inputs/const.txt -s 3 > "$OUT_DIR/const.seed3.width70.len500"
./markov.py ../inputs/const.txt -s 4 -n 1 -w 50 -l 300 > "$OUT_DIR/const.seed4.width50.len300.words1"
./markov.py ../inputs/const.txt -s 4 -w 50 -l 300 -n 3 > "$OUT_DIR/const.seed4.width50.len300.words3"
./markov.py ../inputs/dickinson.txt -s 1 -w 30 -l 100 > "$OUT_DIR/dickinson.seed1.width30.len100"
