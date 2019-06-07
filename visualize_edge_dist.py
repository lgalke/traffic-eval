#!/usr/bin/env python3

"""
File: visualize_edge_dist.py
Author: Lukas Galke
Email: vim@lpag.de
Github: https://github.com/lgalke
Description: Visualize distribution over edges of a routing
"""

import argparse
import os

import numpy as np
from scipy.stats import entropy

import matplotlib
matplotlib.use("Qt5Agg")
import matplotlib.pyplot as plt


def parse_file(path, sort=True):
    edge_counts = []
    with open(path, 'r') as file:
        for line in file:
            line = line.strip()
            if line[0] == '#':
                continue
            edge_id, count = line.split('=')
            edge_counts.append((int(edge_id), int(count)))

    return edge_counts




def main():
    """TODO: Docstring for main.
    :returns: TODO

    """
    "return "

    parser = argparse.ArgumentParser()
    parser.add_argument("usedEdges", nargs='+', help="Path to usedEdges*.txt file")
    args = parser.parse_args()

    plt.figure()

    for path in args.usedEdges: 
        edge_counts = parse_file(path)
        __edge_ids, y = list(zip(*edge_counts))

        y = np.array(sorted(y, reverse=True))
        S = entropy(y, base=2)

        print("H ('{}') = {}".format(path, S))

        x = np.arange(len(y))

        plt.scatter(x, y)
    plt.show()




    
    


if __name__ == "__main__":
    main()
