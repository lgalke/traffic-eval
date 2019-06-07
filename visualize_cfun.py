#!/usr/bin/env python3
"""
File: visualize_cfun.py
Author: Lukas Galke
Email: vim@lpag.de
Github: https://github.com/lgalke
Description: Visualize cost functions
"""
import argparse
import matplotlib
matplotlib.use("Qt5Agg")

from matplotlib import pyplot as plt

import os
import glob

from collections import defaultdict
import itertools as it
from operator import itemgetter

import numpy as np 

def edge_id_from_path(path):
    filename = os.path.basename(path)
    edge_id = os.path.splitext(filename)[0]
    return edge_id


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("path",
                        default='./costFunctions',
                        help="Path to directory with cost functions")

    args = parser.parse_args()


    # To aggregate costs per load globally
    load_costs = defaultdict(float)

    # To aggregate counts per load globally
    # dict with default value 0
    load_counts = defaultdict(int)


    # Dict-of-dicts, with dict generator as default val for outer dict
    # Outer level is keyed by edge ids, inner level by load
    cost_functions = defaultdict(dict)

    for cfn_path in glob.glob(os.path.join(args.path, "*.properties")):
        with open(cfn_path,'r') as cfn_file:
            edge_id = edge_id_from_path(cfn_file.name)
            for line in cfn_file:
                line = line.strip()
                if line[0] == '#':
                    # Comments
                    continue

                # Parse line
                load, rest = line.split('=')
                mean, std, count = rest.split(';')

                # Restore types
                load, mean, count = int(load), float(mean), int(count)

                # Store in edge cost function
                cost_functions[edge_id][int(load)] = mean 

                # Aggregate for global cost function
                # load_costs[load] += mean * count
                # load_counts[load] += count

                load_costs[load] += mean 
                load_counts[load] += 1


    # Compute weighted average of costs wrt accumulated counts
    global_cost_fn = {load: load_costs[load] / load_counts[load] for load in load_costs}

    # Get max len
    print("Max load", max(global_cost_fn))


    # Plotting


    # All cost functions?
    plt.figure(1)
    plt.xlabel("number of vehicles on road segment")
    plt.ylabel("mean traversal time in seconds")
    for cfun in cost_functions.values():
        x, y = zip(*sorted(cfun.items(), key=itemgetter(0)))
        plt.plot(x,y)

    # sort by key and unzip
    x, y = zip(*sorted(global_cost_fn.items(), key=itemgetter(0)))
    plt.plot(x,y, c='b', linewidth=3.0)


    print("#costfunctions =", len(cost_functions))
    plt.show()







if __name__ == "__main__":
    main()
