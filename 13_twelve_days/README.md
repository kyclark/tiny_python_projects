# Twelve Days of Christmas

https://www.youtube.com/playlist?list=PLhOuww6rJJNNZEMX12PE1OvSKy02UQoB4

Write a program that will generate the verse "The Twelve Days of Christmas" song:

```
$ ./twelve_days.py | tail
Ten lords a leaping,
Nine ladies dancing,
Eight maids a milking,
Seven swans a swimming,
Six geese a laying,
Five gold rings,
Four calling birds,
Three French hens,
Two turtle doves,
And a partridge in a pear tree.
```

The program should accept a `-n` or `--number` (default 12) to control the number of verses that are generated:

```
$ ./twelve_days.py -n 2
On the first day of Christmas,
My true love gave to me,
A partridge in a pear tree.

On the second day of Christmas,
My true love gave to me,
Two turtle doves,
And a partridge in a pear tree.
```

A number outside the range 1-12 should be rejected:

```
$ ./twelve_days.py -n 21
usage: twelve_days.py [-h] [-n days] [-o FILE]
twelve_days.py: error: --num "21" must be between 1 and 12
```

If the `-o` or `--outfile` argument is present, the output should be printed to the named file and no output should appear on the command line:

```
$ ./twelve_days.py -o out.txt
```

There should now be an `out.txt` file with the output:

```
$ wc -l out.txt
     113 out.txt
```

The program should respond to `-h` and `--help` with a usage:

```
$ ./twelve_days.py -h
usage: twelve_days.py [-h] [-n days] [-o FILE]

Twelve Days of Christmas

optional arguments:
  -h, --help            show this help message and exit
  -n days, --num days   Number of days to sing (default: 12)
  -o FILE, --outfile FILE
                        Outfile (default: <_io.TextIOWrapper name='<stdout>'
                        mode='w' encoding='utf-8'>)
```

```
$ make test
pytest -xv test.py
============================= test session starts ==============================
...
collected 7 items

test.py::test_exists PASSED                                              [ 14%]
test.py::test_usage PASSED                                               [ 28%]
test.py::test_bad_num PASSED                                             [ 42%]
test.py::test_one PASSED                                                 [ 57%]
test.py::test_two PASSED                                                 [ 71%]
test.py::test_all_stdout PASSED                                          [ 85%]
test.py::test_all PASSED                                                 [100%]

============================== 7 passed in 1.92s ===============================
```
