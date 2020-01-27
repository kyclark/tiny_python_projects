#!/usr/bin/env bash

PRG="./friar.py"

for FILE in tests/*.txt; do
    $PRG $FILE > $FILE.out
done
