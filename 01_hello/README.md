# Chapter 1: Hello, World!

https://www.youtube.com/playlist?list=PLhOuww6rJJNP7UvTeF6_tQ1xcubAs9hvO

Write a program to enthusiastically greet the world:

```
$ ./hello.py
Hello, World!
```

The program should also accept a name given as an optional `--name` parameter:

```
$ ./hello.py --name Universe
Hello, Universe!
```

The program should produce documentation for `-h` or `--help`:

```
$ ./hello.py -h
usage: hello.py [-h] [-n str]

Say hello

optional arguments:
  -h, --help          show this help message and exit
  -n str, --name str  The name to greet (default: World)
```

Run `pytest -xv test.py` (or `make test`) to ensure you pass all the tests:

```
$ make test
pytest -xv test.py
============================= test session starts ==============================
...
collected 4 items

test.py::test_exists PASSED                                              [ 25%]
test.py::test_usage PASSED                                               [ 50%]
test.py::test_default PASSED                                             [ 75%]
test.py::test_input PASSED                                               [100%]

============================== 4 passed in 0.41s ===============================
```
