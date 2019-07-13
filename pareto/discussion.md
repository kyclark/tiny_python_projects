As usual, I use `argparse` to validate all the user arguments and provide reasonable defaults such that the program can run with no input from the user. I pass the `--seed` argumnt directly to `random.seed` and then can worry about how to create and run my simulations.

I decided to create a function `sim` that I would call the correct number of `--round` using a `for` loop. The `sim` function needs to be passed the number of actors, the number of resources, and the target distribution to stop the simulation and will return the number of times through the simulation necessary to reach that target inequality of resource distribution. That is, if there are 10 actors and 10 units, then I stop when 8 units are controlled by no more than 2 actors.

## The simulation

As suggested in the description, I make a `list` to represent the actors:

````
>>> num_actors = 10
>>> num_units = 10
>>> distribution = .8
>>> actors = list(range(1, num_actors + 1))
>>> actors
[1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
````

I need to figure out how many units to initially give each actor:

````
>>> units_per_actor = int(num_units / num_actors)
>>> units_per_actor
1
````

And then `assert` that there is something to distribute:

````
>>> assert units_per_actor > 0, 'Not enough units per actor'
````

I use a dictionary comprehension to create a `dict` that tracks the number of units for each actor:

````
>>> dist
{1: 1, 2: 1, 3: 1, 4: 1, 5: 1, 6: 1, 7: 1, 8: 1, 9: 1, 10: 1}
````

And then set up a `while True` infinite loop. Each time through the loop, I shuffle the actors:

````
>>> random.shuffle(actors)
>>> actors
[7, 1, 9, 2, 10, 3, 5, 6, 8, 4]
````

To create pairs, I use `range` to get every other position and then add `1` to that for the next actor:

````
>>> for i in range(0, len(actors), 2):
...     print(actors[i], actors[i + 1])
...
7 1
9 2
10 3
5 6
8 4
````

Actors can never go into negative values, so I need to ensure both actors still have units:

````
>>> all([dist[a1], dist[a2]])
True
````

If one has no more units, I simply move to the next pair. If they both have assests, I use `random.choice([True, False])` and give 1 unit to the first actor and take 1 from the second if `True`, vice versa if not.

## The distribution

After doing this for all the pairs, I then check the resource distribution with a function called `get_dist` that takes the `dict` of actors/units and the target distribution. Suppose a distribution looks like this:

````
>>> dist
{1: 0, 2: 0, 3: 7, 4: 0, 5: 0, 6: 3, 7: 0, 8: 0, 9: 0, 10: 0}
````

I sort the `values` of the `dict` and find the `sum`

````
>>> values = sorted(list(dist.values()), reverse=True)
>>> values
[7, 3, 0, 0, 0, 0, 0, 0, 0, 0]
>>> total = sum(values)
>>> total
10
````

I figure out how many actors there are and start creating cumulative sums from the beginning of my sorted `values` list, counting how many actors are needed to account for whatever percentage of the total are present:

````
>>> percentile = .8
>>> num_actors = len(values)
>>> for i in range(1, num_actors + 1):
...     cum_sum = sum(values[:i])
...     perc_actors = i / num_actors
...     if cum_sum / total >= percentile:
...         print(i / num_actors)
...         break
...
0.2
````

I can put this into a function:

````
>>> import pareto, inspect
>>> print(inspect.getsource(pareto.get_dist))
def get_dist(dist, percentile):
    """Calculate the distribution of units to actors"""

    values = sorted(list(dist.values()), reverse=True)
    total = sum(values)
    assert total > 0
    num_actors = len(values)

    for i in range(1, num_actors + 1):
        cum_sum = sum(values[:i])
        perc_actors = i / num_actors
        if cum_sum / total >= percentile:
            return i / num_actors

    return 0
````

And test it using the `test_get_dist` function shown earlier.

## Graphing the distribution

Data visualization is a vital part of checking the accuracy of your work. You can use the code you wrote for `histy` to see that, indeed, 80% of the actors have nothing while 20% control everything all due to nothing more than random coin flips:

````
$ ./pareto.py -r 1 -a 10 -u 10 -g graph
  1: 50 iterations
Average = 50 iterations
$ cat graph-1.txt
  1:   0
  2:   0
  4:   0
  5:   0
  6:   0
  7:   0
  8:   0
 10:   0
  9:   2 ##
  3:   8 ########
````

If you run it again, you will most like see that some other two actors were the winners:

````
$ ./pareto.py -r 1 -a 10 -u 10 -g graph
  1: 97 iterations
Average = 97 iterations
$ cat graph-1.txt
  1:   0
  3:   0
  4:   0
  6:   0
  7:   0
  8:   0
  9:   0
 10:   0
  5:   2 ##
  2:   8 ########
````

It doesn't take long for an even distribution to become very skewed. Imagine how much more quickly the imbalance would be achieved if the resources were unevenly distributed at the beginning!

## More

* Find a way to animate the changes to the histogram during each challenge inside the simulation; e.g., `matplotlib.animation` or create a series of GIFs or PNGs that you stitch together to create a short movie to visualize how the resource distribution changes over time.