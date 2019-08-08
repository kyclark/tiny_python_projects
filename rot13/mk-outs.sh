#!/usr/bin/env bash

set -u

PRG="./rot13.py"
FOX="../inputs/fox.txt"
SONNET="../inputs/sonnet-29.txt"
OUT="test-out"

[[ ! -d "$OUT" ]] && mkdir -p "$OUT"

rm $OUT/*

$PRG -S 1 $FOX > "$OUT/fox.txt.out.S1"
$PRG -S 2 -w 30 $FOX > "$OUT/fox.txt.out.S2.w30"
$PRG -S 3 -p5 -w 25 $FOX > "$OUT/fox.txt.out.S3.p5.w25"
$PRG -S 4 -s 5 $FOX > "$OUT/fox.txt.out.S4.s5"

$PRG -S 1 $SONNET > "$OUT/sonnet.txt.out.S1"
$PRG -S 2 -w 30 $SONNET > "$OUT/sonnet.txt.out.S2.w30"
$PRG -S 3 -p5 -w 25 $SONNET > "$OUT/sonnet.txt.out.S3.p5.w25"
$PRG -S 4 -s 5 $SONNET > "$OUT/sonnet.txt.out.S4.s5"
