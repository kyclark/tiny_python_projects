# Rock, Paper, Scissors

Write a Python program called `rps.py` that will play the ever-popular "Rock, Paper, Scissors" game. As often as possible, insult the player by combining an adjective and a noun from the following lists:

Adjectives =
truculent fatuous vainglorious fatuous petulant moribund jejune
feckless antiquated rambunctious mundane misshapen glib dreary
dopey devoid deleterious degrading clammy brazen indiscreet
indecorous imbecilic dysfunctional dubious drunken disreputable
dismal dim deficient deceitful damned daft contrary churlish
catty banal asinine infantile lurid morbid repugnant unkempt
vapid decrepit malevolent impertinent decrepit grotesque puerile

Nouns =
abydocomist bedswerver bespawler bobolyne cumberworld dalcop
dew-beater dorbel drate-poke driggle-draggle fopdoodle fustylugs
fustilarian gillie-wet-foot gnashgab gobermouch
gowpenful-o’-anything klazomaniac leasing-monger loiter-sack
lubberwort muck-spout mumblecrust quisby raggabrash rakefire
roiderbanks saddle-goose scobberlotcher skelpie-limmer
smell-feast smellfungus snoutband sorner stampcrab stymphalist
tallowcatch triptaker wandought whiffle-whaffle yaldson zoilist

The program should accept a `-s|--seed` to pass to `random`.

````
$ ./rps.py
1-2-3-Go! [rps|q] r
You: Rock
Me : Scissors
You win. You are a clammy drate-poke.
1-2-3-Go! [rps|q] t
You dysfunctional dew-beater! Please choose from: p, r, s.
1-2-3-Go! [rps|q] p
You: Paper
Me : Rock
You win. You are a dismal gillie-wet-foot.
1-2-3-Go! [rps|q] q
Bye, you imbecilic fopdoodle!
````
