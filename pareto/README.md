# Modeling the Pareto Principle


Vilfredi Pareto was an Italian economist who noted in the late 1800s that roughly 80% of the land in Italy was owned by about 20% of the population. This 80/20 rule has been noted in many other contexts, but it stands out in wealth inequalities where it has tilted ever further to 90/10 or even 99/1. This exercise is designed to simulate the move of resources to an ever shrinking segment of a population through random events.

In our exercise, we will create variables to represent the following:

1. The number of actors in the simulation
2. The number of units of some resource
3. The percent of unequal distribution to stop the simulation
4. The number of iterations of the simulation to run

Create a program called `pareto.py` that accepts options for the number of `-a|--actors` (default `50`), the number of `-u|--units` (default `500`), the target `-d|--distribution` (default `0.8`), the number of `-r|--rounds` to simulate (default `10`). You also need to accept a `-s|--seed` option to pass to `random.seed` (default `None`) and an option to `-g|--graph` the result of each simulation as a text histogram to some file base name (default `None`).

The "resource" at play could be thought of as some measure of wealth or some resource like food. Ours is a zero-sum simulation where all the actors are randomly paired with each other and a coin is flipped to determine a winner. Each loser gives up one unit to the winner. Actors with no more units can no longer participate, so they cannot go into negative values ("debt") but neither can they ever re-enter the game. 

## The simulation

At the beginning of each simulation, the `--units` should evenly distributed to all the `--actors`. Create an infinite loop where the actors are shuffled and then paired up. I suggest you represent the actors as a `list` that you can pass to the `random.shuffle` function. To create the pairs, think about using the `range` function with a step value of `2` to get the position of every other actor, and then the mate for each will be the one just after it. "Flip" a coin by using `random.choice([True, False])`. If `True`, give the first player one unit and subtract one unit from the second; if `False,` vice versa. Consider using a `dict` to keep track of the number of units for each actor.

Each simulation is done when the designated `distribution` (default `0.8` or 80%) is controlled by `1 - distribution` (`0.2` or 20%). So when 80% of the units are controlled by 20% of the actors, return the number of iterations through the infinite loop it took to reach the target.

## Calculating the distribution

If there are 10 actors and 10 units, the distribution starts out looking like this:

````
>>> units = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1]
````

You should stop when 2 actors control all the assets, so something like this:

````
>>> units = [0, 0, 7, 0, 0, 3, 0, 0, 0, 0]
````

Think about sorting the units from largest to smallest and then checking cumulative sums starting from the start. When the sum is greater than the target percentage, divide the number of values that went in by the total number of values to find the percentage controlling the target amount.

Consider adding a test, e.g., if the function is called `get_dist` then you can create the following to run with `pytest`:

````
def test_get_dist():
    """Test get_dist"""

    tests = [
        ([1, 1, 1, 1, 1, 1, 1, 1, 1, 1], 0.8, 0.8),
        ([2, 2, 2, 1, 0, 0, 0, 0, 0, 0], 0.8, 0.3),
        ([2, 2, 2, 2, 2, 0, 0, 0, 0, 0], 1.0, 0.5),
        ([0, 0, 7, 0, 0, 3, 0, 0, 0, 0], 0.8, 0.2),
        ([0, 0, 9, 0, 0, 1, 0, 0, 0, 0], 0.9, 0.1),
    ]

    for vals, perc, target in tests:
        dist = {k:v for k,v in enumerate(vals, 1)}
        assert get_dist(dist, perc) == target
````

Hints:

* For the `--graph` option, you should be able to use your `histy` code exactly.
* Consider make a function that runs one simulation, then call that function for the number in `--rounds`