#!/usr/bin/env bash

PRG='./bottles.py'

if [[ ! -f "$PRG" ]]; then
    echo "Missing \"$PRG\""
    exit 1
fi

for i in $(seq 1 5); do
    printf "%s\t%s\n" $i $($PRG -n $i | md5)
done
