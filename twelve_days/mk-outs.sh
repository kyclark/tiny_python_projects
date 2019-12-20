#!/usr/bin/env bash

set -u

PRG="./twelve_days.py"
OUT="test-out"

[[ ! -d "$OUT" ]] && mkdir -p "$OUT"

for i in $(seq 1 12); do
    echo "$i"
    $PRG -n $i -o "$OUT/$i.out"
done

echo "Done."
