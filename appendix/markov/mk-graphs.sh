#!/usr/bin/env bash

PRG="./graph.py"
INPUT="words.txt"

for K in 1 2 3 4; do
    $PRG -k $K -o "$K-out.gv" "$INPUT"
done

echo "Done."
