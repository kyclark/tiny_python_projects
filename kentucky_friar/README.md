# Kentucky Fryer

Write a Python program called `fryer.py` that reads some input text from a single positional argument on the command line (which could be a file to read) and transforms the text by dropping the "g" from words two-syllable words ending in "-ing" and also changes "you" to "y'all". Be mindful to keep the case the same on the first letter, e.g, "You" should become "Y'all," "Hunting" should become "Huntin'".

````
$ ./fryer.py
usage: fryer.py [-h] str
fryer.py: error: the following arguments are required: str
$ ./fryer.py -h
usage: fryer.py [-h] str

Southern fry text

positional arguments:
  str         Input text or file

optional arguments:
  -h, --help  show this help message and exit
$ ./fryer.py you
y'all
$ ./fryer.py Fishing
Fishin'
$ ./fryer.py string
string
$ cat tests/input1.txt
So I was fixing to ask him, "Do you want to go fishing?" I was dying
to go for a swing and maybe do some swimming, too.
$ ./fryer.py tests/input1.txt
So I was fixin' to ask him, "Do y'all want to go fishing?" I was dyin'
to go for a swing and maybe do some swimmin', too.
````
