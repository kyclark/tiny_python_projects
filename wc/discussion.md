This program is rather short and seems rather simple, but it's definitely not exactly easy. The point of the exercise is to really get familiar with `argparse` and the trouble it can save you. The key is in defining the `file` positional arguments. If you use `nargs='*'` to indicate zero or more arguments, then you know `argparse` is going to give you back a `list` with zero or more elements. If you use `type=argparse.FileType('r')` then any arguments given must be readable files. The `list` that `argparse` returns will be a `list` of *open file handles*. Lastly, if you use `default=[sys.stdin]`, then you understand that `sys.stdin` is essentially an open file handle to read from "standard in" (AKA `STDIN`), and you are letting `argparse` know that you want the default to be a `list` containing `sys.stdin`.

I can fake `args.file` in the REPL, and then use a `for` loop to iterate through them. On each one, I initialize three variables with zeros to hold the count of lines, characters, and words. I then use another `for` loop to iterate over each line in the file handle (`fh`). I can add `1` on each iteration to increment the `lines` variable. The length of the line (`len(line)`) is the number of characters which can be added to `chars`. Lastly `line.split()` will break the line on whitespace which is close enough to "words", and the length of the resulting `list` is the number of words on the line which is added to `words`. The `for` loop ends when the end of the file is reached, and that is when I can `print` out the counts and the file name using `{:8}` placeholders in the print template to indicate a text field 8 characters wide:

````
>>> files = [open('../inputs/fox.txt')]
>>> for fh in files:
...     lines, words, chars = 0, 0, 0
...     for line in fh:
...         lines += 1
...         chars += len(line)
...         words += len(line.split())
...     print('{:8}{:8}{:8} {}'.format(lines, words, chars, fh.name))
...
       1       9      45 ../inputs/fox.txt
````

## Further

Implement other system tools like `cat` and `head`.