#!/usr/bin/env bash

TESTS=$(mktemp)
find . -mindepth 2 -maxdepth 2 -name all_test.sh | sort > "$TESTS"

while read -r TEST; do
    DIR=$(dirname "$TEST")
    echo -e "\n\n==> $DIR <==\n\n"
    (cd "$DIR" && ./all_test.sh)
done < "$TESTS"

rm "$TESTS"
