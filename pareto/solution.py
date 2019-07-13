#!/usr/bin/env python3
"""Simulation of Pareto distribution through random simulation"""

import argparse
import random


# --------------------------------------------------
def get_args():
    """Get command-line arguments"""

    parser = argparse.ArgumentParser(
        description='Argparse Python script',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    parser.add_argument('-a',
                        '--actors',
                        help='Number of actors',
                        metavar='int',
                        type=int,
                        default=50)

    parser.add_argument('-u',
                        '--units',
                        help='Number of units',
                        metavar='int',
                        type=int,
                        default=500)

    parser.add_argument('-d',
                        '--distribution',
                        help='Target distribution',
                        metavar='float',
                        type=float,
                        default=0.8)

    parser.add_argument('-r',
                        '--rounds',
                        help='Number of rounds',
                        metavar='int',
                        type=int,
                        default=10)

    parser.add_argument('-s',
                        '--seed',
                        help='Random seed',
                        metavar='int',
                        type=int,
                        default=None)

    parser.add_argument('-g',
                        '--graph',
                        help='Show histograms',
                        action='store_true')

    return parser.parse_args()


# --------------------------------------------------
def main():
    """Make a jazz noise here"""

    args = get_args()
    random.seed(args.seed)

    results = []
    for i in range(args.rounds):
        res = sim(num_actors=args.actors,
                  num_units=args.units,
                  distribution=args.distribution,
                  graph=args.graph)

        print('{:3}: {}'.format(i + 1, res))
        results.append(res)

    print('Average = {}'.format(sum(results) / len(results)))


# --------------------------------------------------
def sim(num_actors, num_units, distribution, graph=False):
    """Run a simulation"""

    actors = list(range(1, num_actors + 1))
    units_per_actor = int(num_units / num_actors)
    dist = {actor: units_per_actor for actor in actors}

    while True:
        random.shuffle(actors)
        for i in range(0, len(actors), 2):
            a1, a2 = actors[i], actors[i + 1]
            if dist[a1] and dist[a2]:
                res = random.choice([0, 1])
                dist[a1] += 1 if res else -1
                dist[a2] += 1 if res else -1

            if get_dist(dist, percentile=distribution) <= 1 - distribution:
                print('Reached {} in {}'.format(distribution, i + 1))
                if graph:
                    for units, actor in sorted([(v, k)
                                                for k, v in dist.items()]):
                        print('{:3}: {:3} {}'.format(actor, units,
                                                     '#' * units))
                return i + 1

    return 0


# --------------------------------------------------
def get_dist(dist, percentile=.8):
    """Calculate the distribution of units to actors"""

    # 1 - (x_m / x) ** alpha
    # return 1 - (scale / percentile) ** alpha

    values = sorted(list(dist.values()), reverse=True)
    total = sum(values)
    num_actors = len(values)
    for i in range(1, num_actors + 1):
        cum_sum = sum(values[:i])
        if cum_sum / total >= percentile:
            return i / num_actors

    return 0


# --------------------------------------------------
if __name__ == '__main__':
    main()
