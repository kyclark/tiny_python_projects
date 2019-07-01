!["To alcohol! The cause of, and solution to, all of life's problems." - H. Simpson](images/beer.png)

If you used `new.py` and `argparse` to get started, then about 1/4 of the program is done for you. If you define an argument with the appropriate "short" (a dash plus one character) and "long" names (two dashes and a longer bit) with `type=int` and `default=10`, then `argparse` will do loads of hard work to ensure the user provides you with the correct input. We can't easily tell `argparse` that the number has to be a *positive* integer without defining a new "type", but it's fairly painless to add a check and use `parser.error` to both print an error message plus the usage and halt the execution of the program.

Earlier programs have the last line of `get_args` as:

````
return parser.parse_args()
````

But here we capture the arguments inside `get_args` and add a bit of validation. If `args.num_bottles` is less than one, we call `parser.error` with the message we want to tell the user. We don't have to tell the program to stop executing as `argparse` will exit immediately. Even better is that it will indicate a non-zero exit value to the operating system to indicate there was some sort of error. If you ever start writing command-line programs that chain together to make workflows, this is a way for one program to indicate failure and halt the entire process until the error has been fixed!

Once you get to the line `args = get_args()` in `main`, a great deal of hard work has already occurred to get and validate the input from the user. From here, I decided to create a template for the song putting `{}` in the spots that change from verse to verse. Then I use the `reversed(range(...))` bit we discussed before to count down, with a `for` loop, using the current number `bottle` and `next_bottle` to print out the verse noting the presence or absence of the `s` where appropriate.
