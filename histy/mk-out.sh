#!/usr/bin/env bash

PRG="./histy.py"
OUT="./out"

./$PRG 3 1 2 > "$OUT/1.out"
./$PRG 4 12 3 5 9 11 > "$OUT/2.out"
./$PRG 444 132 323 125 99 141 -s 10 > "$OUT/3.out"
./$PRG 239 336 100 34 89 -s 5 -m 100 -c '*' > "$OUT/4.out"
./$PRG 44 32 87 23 19 -s 2 -c '!' > "$OUT/5.out"
