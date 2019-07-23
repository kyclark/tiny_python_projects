There's not much to say about `get_args` at this point. The `-t|--tiles` is a `str` which can only be 7 characters maximum, so I check `args.tiles` and use `parser.error` to generate a usage, error, and to exit with an non-zero status.

## Organizing the wordlist

The `--wordlist` file is expected to be a standard dictionary file with single words on  each line, but it might be something else so I use `fh.read().upper().split()` to force all the text to uppercase and break it at whitespace into words. The purpose of the wordlist is to find words I can make from a given set of tiles. If I have 2 tiles, then I want to make 3-letter words; 4 tiles then 5-letter words, etc. Therefore it makes sense to organize all the words by their lengths. I will reach for the `defaultdict` from the `collections` module where the keys will be the length of each word and the values will be a `list` of the words that length.

````
>>> from collections import defaultdict
>>> words = defaultdict(list)
````

For purposes of illustration and testing, I will use a mock file handle with the `io.StringIO` function:

````
>>> import io
>>> fh = io.StringIO('apple banana cherry fig')
````

I will iterate over each word in the file handle and `append` it to the `list` identified by the `len(word)`. Additionally, I decided to use a `Counter` also from the `collections` module to help me identify words