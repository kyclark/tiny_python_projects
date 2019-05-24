# Family Tree

Write a program called `tree.py` that will take an input file as a single positional argument and produce a graph of the family tree described therein. The file can have only three kinds of statements:

1. `INITIALS = Full Name`
2. `person1 married person2`
3. `person1 and person2 begat child1[, child2...]`

Use the `graphviz` module to generate a graph like the `kyc.gv.pdf` included here that was generated from the following input:

````
$ cat kyc.txt
EM = Ewell Magee
MLB = Mary Lulu Bond
EBM = Elizabeth Magee
BJM = Jean Magee
DWM = Durwood Magee
MAM = Martha Magee
EVM = Evelyn Magee
EY = Ernest Youens
MRY = Mrs. Youens
BY = Bob Youens
CY = Charlie Youens
JY = John Youens
KYC = Ken Youens-Clark
NCY = Nancy Youens

EM married MLB
EM and MLB begat EBM, BJM, DWM, MAM, EVM
MAM married CY
CY and MAM begat KYC
EY and MRY begat BY, CY, JY
EY married MRY
JY married NCY
````
