#!/usr/bin/env bash

set -u

PRG="./histy.py"
OUT="./test-outs"
FOX="../inputs/fox.txt"
SONNET="../inputs/sonnet-29.txt"

$PRG $FOX > "$OUT/fox.txt.1"
$PRG -i $FOX > "$OUT/fox.txt.2"
$PRG -c '!' $FOX > "$OUT/fox.txt.3"
$PRG -m 2 $SONNET > "$OUT/sonnet-29.txt.1"
$PRG -w 50 -c '$' -f -m 2 $SONNET > "$OUT/sonnet-29.txt.2"
