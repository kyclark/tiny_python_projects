# File Handles

A file's name is a string like `'nobody.txt'`. To read or write the contents of the file, you need a *file handle* which you can get from `open`. Think of a file name as the address of your house. It's where your house can be found, but I can't know what's in your house unless I go there and open the door. That's what `open` does -- it finds the file's bits on disk and opens the door to read or write the file.

## File Modes

By default, a file is opened in *read* mode which means that it can't be altered. Also, the default is to open for reading *text*.  The only required argument to `open` is the file name, but a second optional argument is a combination of characters to explain how to open the file. From the documentation for `open`:

````
========= ===============================================================
Character Meaning
--------- ---------------------------------------------------------------
'r'       open for reading (default)
'w'       open for writing, truncating the file first
'x'       create a new file and open it for writing
'a'       open for writing, appending to the end of the file if it exists
'b'       binary mode
't'       text mode (default)
'+'       open a disk file for updating (reading and writing)
'U'       universal newline mode (deprecated)
========= ===============================================================
````

So if you do:

````
fh = open('out.txt')
````

It's the same as doing:

````
fh = open('out.txt', 'wt')
````

Where the combination of `wt` means `write text`. We can also read and write raw bits in `binary`, e.g., if you wanted to read the bit values of the pixels in an image.

I always make a distinction in the variable names for the `file` or `filename` and the *file handle* which I usually call `fh` if there's just one or maybe `in_fh` and `out_fh` if there is one for reading and one for writing, etc.

## STDIN, STDOUT, STDERR

Unix has three standard files or channels called *standard in*, *standard out*, and *standard error* which are normally written as STDIN, STDOUT, and STDERR. When you `print`, the default is that the text goes to STDOUT which you see in your terminal or REPL.

The `print` function takes some optional keyword arguments, one of which is `file` which has the default value of `sys.stdout`. If you wish to `print` to *standard error* (STDERR), you can use the `sys.stderr` file:

````
print('This is an error!', file=sys.stderr)
````

Note that you *do not* have to `open` these two special file handles. They are always available to you. 

If you wish to write to a file on disc, you can `open` a file for writing and pass that:

````
print('This is an error!', file=open('error.txt', 'wt'))
````

Note that if each time you `open` a file for writing, you overwrite any existing data. If you wanted to `print` repeatedly in a program, you would either need to `open` in append mode:

````
print('This is an error!', file=open('error.txt', 'at'))
print('This is an also error!', file=open('error.txt', 'at'))
````

Or, better yet, `open` the file at the beginning of the program, `print` as often as you like, and then `close` the file:

````
fh = open('out.txt', 'wt')
print('Writing some text.', file=fh)
print('Adding more text.', file=fh)
fh.close()
````

Or use the `write` method of the file handle:

````
fh = open('out.txt', 'wt')
fh.write('Writing some text.\n')
fh.write('Adding more text.\n')
fh.close()
````

Note that `print` automatically adds a newline to the end of the text whereas `write` does not so you need to add it yourself.

You can only *read* from STDIN. Again, you do not need to `open` it as it is always available. Treat it exactly like a file handle you've opened for reading, e.g., to read lines from STDIN until you recieve EOF (end of file):

````
for line in sys.stdin:
````
