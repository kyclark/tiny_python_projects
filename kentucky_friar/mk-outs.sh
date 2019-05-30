#!/usr/bin/env bash

PRG="./friar.py"

for FILE in tests/*; do
    $PRG $FILE > $FILE.out
done
