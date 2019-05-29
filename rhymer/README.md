# Simple Rhymer

Write a Python program called `rhymer.py` that will create new words by removing the consonant(s) from the beginning of the word and then creating new words by prefixing the remainder with all the consonants and clusters that were not at the beginning. That is, prefix with all the consonants in the alphabet plus these clusters:

    bl br ch cl cr dr fl fr gl gr pl pr sc sh sk sl sm sn sp 
    st sw th tr tw wh wr sch scr shr sph spl spr squ str thr

````
$ ./rhymer.py
usage: rhymer.py [-h] str
rhymer.py: error: the following arguments are required: str
$ ./rhymer.py -h
usage: rhymer.py [-h] str

Make rhyming "words"

positional arguments:
  str         A word

optional arguments:
  -h, --help  show this help message and exit
$ ./rhymer.py apple
Word "apple" must start with consonants  
$ ./rhymer.py take | head
bake
cake
dake
fake
gake
hake
jake
kake
lake
make
````
