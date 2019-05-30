#!/usr/bin/env bash

PRG="./fryer.py"

for FILE in tests/*; do
    $PRG $FILE > $FILE.out
done
