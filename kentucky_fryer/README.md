# Kentucky Fryer

Write a Python program called `fryer.py` that reads some input text from a single positional argument on the command line (which could be a file to read) and transforms the text by dropping the "g" from words two-syllable words ending in "-ing" and also changes "you" to "y'all".

````
$ cat test.txt
So I was fixing to ask him, "Do you want to go fishing?" I was dying
to go for a swing and maybe do some swimming, too.
$ ./fryer.py test.txt
So I was fixin' to ask him, "Do y'all want to go fishing?" I was dyin'
to go for a swing and maybe do some swimmin', too.
````
