#!/usr/bin/env python3

"""
File: visualize_driving_times.py
Author: Lukas Galke
Email: vim@lpag.de
Github: https://github.com/lgalke
Description: Visualize driving times
"""

import argparse
import os

import numpy as np
from scipy.stats import entropy, ttest_ind

import matplotlib
matplotlib.use("Qt5Agg")
import matplotlib.pyplot as plt


def parse_file(path, sort=True):
    with open(path, 'r') as file:
        driving_times = [float(line.strip()) for line in file]
    return driving_times



def stats(x):
    x = np.asarray(x)
    mean, std = x.mean(), x.std(ddof=1)
    q0, q25, q50, q75, q100 = np.quantile(x, [0., .25, .5, .75, 1.])
    se = std / np.sqrt(x.size)
    se95 = 1.96 * se
    return (mean, se95, std, q0, q25, q50, q75, q100)


stats_summary = "Mean: {:.2f} +- {:.2f}, SD: {:.2f}, Min: {:.2f}, Q25: {:.2f}, Median: {:.2f}, Q75: {:.2f}, Max: {:.2f}"


def main():
    """TODO: Docstring for main.
    :returns: TODO

    """
    "return "

    parser = argparse.ArgumentParser()
    parser.add_argument("drivingTimes", nargs='+', help="Path to drivingTimes*.txt file")
    parser.add_argument("--legend", nargs='+', default=None, help="Specify legend *IN SAME ORDER* as input files")
    args = parser.parse_args()

    plt.figure()

    previous = []

    for i, path in enumerate(args.drivingTimes):
        driving_times = parse_file(path)

        y = np.array(sorted(driving_times, reverse=True))

        S = entropy(y)

        desc = path if not args.legend else args.legend[i]

        print("Stats for '{}'".format(desc))
        print("Entropy: {}".format(S))
        print(stats_summary.format(*stats(y)))


        x = np.arange(len(y))

        plt.scatter(x, y, marker='.')


        for prev_path, prev_y in previous:
            print("t-test('{}','{}')".format(desc, prev_path))
            print("p = {}".format(ttest_ind(y, prev_y)))


        previous.append((desc, y))

    if args.legend:
        plt.legend(args.legend)
    plt.xlabel("Drivers")
    plt.ylabel("Time in seconds")
    plt.show()




    
    


if __name__ == "__main__":
    main()

