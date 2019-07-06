# Mad Libs

![This definitely not a copyright infringment.](images/mad_libs.png)

Write a Python program called `mad_lib.py` that will read a file given as a positional argument and find all the placeholders noted in `<>`, e.g., `<verb>`, prompt the user for the part of speech being requested, e.g., a "verb", and then substitute that into the text of the file, finally printing out all the placeholders replaced by the user's inputs. By default, this is an interactive program that will use the `input` prompt to ask the user for their answers, but, for testing purposes, you will have an option for `-i|--inputs` so the test suite can pass in all the answers and bypass the `input` calls.

Given no arguments or the `-h|--help` flag, the program should print a usage:

````
$ ./mad_lib.py
usage: mad_lib.py [-h] [-i str [str ...]] FILE
mad_lib.py: error: the following arguments are required: FILE
$ ./mad_lib.py -h
usage: mad_lib.py [-h] [-i str [str ...]] FILE

Mad Libs

positional arguments:
  FILE                  Input file

optional arguments:
  -h, --help            show this help message and exit
  -i str [str ...], --inputs str [str ...]
                        Inputs (for testing) (default: None)
````

The structure of the input file has a part of speech enclosed in angle brackets, e.g., `<verb>`:

````
$ cat help.txt
<exclamation>! I need <noun>!
<exclamation>! Not just <noun>!
<exclamation>! You know I need <noun>!
<exclamation>!
````

When this is the input for the program, you should ask for each part of speech in order using the `input` command to ask the user for some text. When you've gotten all the text you need, print out the result of putting the user's answers into the placeholders:	
	
````
$ ./mad_lib.py help.txt
exclamation: Hey
noun: tacos
exclamation: Oi
noun: fish
exclamation: Ouch
noun: pie
exclamation: Dang
Hey! I need tacos!
Oi! Not just fish!
Ouch! You know I need pie!
Dang!
````

The default mode is to be interactive, which is difficult to test, so take all the  `--inputs` from the command line, skip the `input` prompts, and just show the resulting text:

````
$ ./mad_lib.py romeo_juliet.txt -i cars Detroit oil pistons \
> "stick shift" furious accelerate 42 foot hammer
Two cars, both alike in dignity,
In fair Detroit, where we lay our scene,
From ancient oil break to new mutiny,
Where civil blood makes civil hands unclean.
From forth the fatal loins of these two foes
A pair of star-cross'd pistons take their life;
Whose misadventur'd piteous overthrows
Doth with their stick shift bury their parents' strife.
The fearful passage of their furious love,
And the continuance of their parents' rage,
Which, but their children's end, nought could accelerate,
Is now the 42 hours' traffic of our stage;
The which if you with patient foot attend,
What here shall hammer, our toil shall strive to mend.
````

Hints:

* Definitely look into using regular expressions!
