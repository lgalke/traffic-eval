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
        for i, line in enumerate(file):
            line = line.strip()
            if line[0] == '#':
                continue
            try:
                edge_id, count = line.split('=')
            except ValueError:
                print("Parse error in line", i+1, "of file", file.name)
                continue
            edge_counts.append((int(edge_id), int(count)))

    return edge_counts




def main():
    """TODO: Docstring for main.
    :returns: TODO

    """
    "return "

    parser = argparse.ArgumentParser()
    parser.add_argument("usedEdges", nargs='+', help="Path to usedEdges*.txt file")
    parser.add_argument("--legend", nargs='+', default=None, help="Specify legend *IN SAME ORDER* as input files")
    args = parser.parse_args()

    plt.figure()

    for i, path in enumerate(args.usedEdges): 
        edge_counts = parse_file(path)
        __edge_ids, y = list(zip(*edge_counts))

        desc = args.legend[i] if args.legend else path

        y = np.array(sorted(y, reverse=True))
        S = entropy(y, base=2)
        print("H ('{}') = {}, N={}".format(desc, S, y.size))

        x = np.arange(len(y))

        plt.scatter(x, y, marker='.')

    if args.legend:
        plt.legend(args.legend)

    plt.xlabel("Road segments")
    plt.ylabel("#routes on segment")
    plt.show()




    
    


if __name__ == "__main__":
    main()
