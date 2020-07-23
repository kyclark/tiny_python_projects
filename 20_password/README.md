# Password

https://www.youtube.com/playlist?list=PLhOuww6rJJNMRNnUQyUkGjpztCBUCiwZt

Cf. https://xkcd.com/936/

Create a program that will randomly combine words from given text(s) to create novel, memorable, unbreakable passwords:

```
$ ./password.py
EchinochloaJapeCollinglyRadiotrician
EthanedithiolRefleePrebudgetPolyphonism
BerriChamaecyparisOutdraftArcifera
```

By default, the program should read the standard word dictionary `/usr/share/dict/words` for the word list but should also accept optional positional arguments.
The program should create a list of unique words with all non-word characters removed, randomly select some `-w` or `--num_words` for each password, and join the titlecased selections into new passwords:

```
$ ./password.py -w 3 scarlet/*
ShouldOfferPeculiar
LongDeathWill
LikeVenerableBear
```

The words selected should have a `-m` or `--min_word_len` that defaults to 3 in order to remove short, unmemorable words:

```
$ ./password.py -m 5 sonnets/*
IndigestPublishPaintingParticular
AccidentImprintDancePosterity
ExcuseGrossStateLaughd
```

The program should accept a `-n` and `--num` flag to control the number of passwords that are created:

```
$ ./password.py -n 2 const/*
NumberFollowExtraordinaryCompel
ThinkLegislationAppellateEligible
```

Be sure to accept a `-s` or `--seed` option to use as the random seed to ensure reproducibility:

```
$ ./password.py -s 1
ChromePorometerUnwastableUnconditionated
ThujaAwesomelyEyeglanceCatabolin
OptiveThicketMoratoriaNoncompetent
```

If the `--l33t` flag is present, the passwords should be obfuscated by:

1. Using the "ransom" algorightm from chapter 13
2. Using a character substitution as in chapter 5
3. Add a randomly selected punctuation at the end

Here is the substitution table:

```
a => @
A => 4
o => 0
O => 0
t => +
e => 3
E => 3
I => 1
S => 5
```

Here is what the output would look like without:

```
$ ./password.py sonnets/* -s 1
EagerCarcanetLilyDial
WantTempestTwireRondure
HealCrawlVerdictBase
```

And the same passwords with the encoding:

```
$ ./password.py sonnets/* -s 1 --l33t
34G3rc4rC4n3TliLydi@L.
5p0r+1V3B@sT@RDhURT5uFf3Rd\
rh3T0r1cC0n+3ndsU1T3Dw1l+`
```

The program should print a usage for the `-h` and `--help` flags:

```
$ ./password.py -h
usage: password.py [-h] [-n int] [-w int] [-m int] [-s int] [-l]
                   [FILE [FILE ...]]

Password maker

positional arguments:
  FILE                  Input file(s) (default: [<_io.TextIOWrapper
                        name='/usr/share/dict/words' mode='r'
                        encoding='UTF-8'>])

optional arguments:
  -h, --help            show this help message and exit
  -n int, --num int     Number of passwords to generate (default: 3)
  -w int, --num_words int
                        Number of words to use for password (default: 4)
  -m int, --min_word_len int
                        Minimum word length (default: 4)
  -s int, --seed int    Random seed (default: None)
  -l, --l33t            Obfuscate letters (default: False)
```

Run the test suite to ensure your program is correct:

```
$ make test
pytest -xv test.py
============================= test session starts ==============================
...
collected 7 items

test.py::test_exists PASSED                                              [ 14%]
test.py::test_usage PASSED                                               [ 28%]
test.py::test_bad_file PASSED                                            [ 42%]
test.py::test_bad_num PASSED                                             [ 57%]
test.py::test_bad_num_words PASSED                                       [ 71%]
test.py::test_bad_min_word_len PASSED                                    [ 85%]
test.py::test_bad_seed PASSED                                            [100%]

============================== 7 passed in 0.46s ===============================
```
