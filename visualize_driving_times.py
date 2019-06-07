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
from scipy.stats import entropy

import matplotlib
matplotlib.use("Qt5Agg")
import matplotlib.pyplot as plt


def parse_file(path, sort=True):
    with open(path, 'r') as file:
        driving_times = [float(line.strip()) for line in file]
    return driving_times



def stats(x):
    x = np.asarray(x)
    mean, std = x.mean(), x.std()
    q0, q25, q50, q75, q100 = np.quantile(x, [0., .25, .5, .75, 1.])
    return (mean, std, q0, q25, q50, q75, q100)


stats_summary = "Mean: {:.2f}, SD: {:.2f}, Min: {:.2f}, Q25: {:.2f}, Median: {:.2f}, Q75: {:.2f}, Max: {:.2f}"


def main():
    """TODO: Docstring for main.
    :returns: TODO

    """
    "return "

    parser = argparse.ArgumentParser()
    parser.add_argument("drivingTimes", nargs='+', help="Path to drivingTimes*.txt file")
    args = parser.parse_args()

    plt.figure()

    for path in args.drivingTimes: 
        driving_times = parse_file(path)

        y = np.array(sorted(driving_times, reverse=True))
        S = entropy(y, base=2)

        print("Stats for '{}'".format(path))
        print("Entropy: {}".format(S))
        print(stats_summary.format(*stats(y)))


        x = np.arange(len(y))

        plt.scatter(x, y)
    plt.xlabel("Drivers")
    plt.ylabel("Time in seconds")
    plt.show()




    
    


if __name__ == "__main__":
    main()

