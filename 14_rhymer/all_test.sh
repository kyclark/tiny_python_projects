#!/usr/bin/env bash

set -eu -o pipefail

PRG="rhymer.py"
for FILE in solution[12]_*.py; do
    echo "==> ${FILE} <==" 
    cp "$FILE" "$PRG"
    make test
done

echo "Done."
