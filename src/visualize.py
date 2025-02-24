#!/usr/bin/env python3

# command line args
import argparse
parser = argparse.ArgumentParser()
parser.add_argument('--input_path', required=True)
parser.add_argument('--key', required=True)
parser.add_argument('--percent', action='store_true')
args = parser.parse_args()

# imports
import os
import json
import matplotlib.pyplot as plt
from collections import Counter, defaultdict

# open the input path
with open(args.input_path) as f:
    counts = json.load(f)

# normalize the counts by the total values if --percent is used
if args.percent:
    for k in counts[args.key]:
        counts[args.key][k] /= counts['_all'][k]

# sort the counts
items = sorted(counts[args.key].items(), key=lambda item: (item[1], item[0]), reverse=True)

# print the counts
for k, v in items:
    print(k, ':', v)

# Prepare data for plotting (Top 10)
labels, values = zip(*items[:10])

# Plotting
plt.figure(figsize=(10, 6))
plt.barh(labels, values, color='skyblue')
plt.xlabel('Number of Tweets')
plt.title(f"Top 10 for {args.key}")
plt.tight_layout()

# Save plot as PNG
output_filename = f"{args.key.strip('#')}.png"
plt.savefig(output_filename)
print(f"Plot saved as {output_filename}")
