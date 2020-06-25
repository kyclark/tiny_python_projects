#!/usr/bin/env bash

TESTS=$(mktemp)
find . -name all_test.sh > "$TESTS"

while read -r TEST; do
    DIR=$(dirname "$TEST")
    echo -e "\n\n==> $DIR <==\n\n"
    (cd "$DIR" && ./all_test.sh)
done < "$TESTS"

rm "$TESTS"
