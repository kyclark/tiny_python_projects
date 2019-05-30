#!/usr/bin/env bash

PRG="./transpose.py"

for SONG in songs/*.abc; do
    BASE=$(basename "$SONG")
    echo "$BASE"

    for INT in 2 4 -5; do
        $PRG "$SONG" -s "$INT" > "songs/$BASE.$INT.out"
    done
done

echo "Done."
