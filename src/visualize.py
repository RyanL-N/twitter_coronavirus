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

# open the input path
with open(args.input_path) as f:
    counts = json.load(f)

# normalize the counts by the total values
if args.percent:
    for k in counts[args.key]:
        counts[args.key][k] /= counts['_all'][k]

# sort and prepare data
items = sorted(counts[args.key].items(), key=lambda item: (item[1], item[0]), reverse=True)
keys = [k for k, v in items[:10]]
values = [v for k, v in items[:10]]

# plotting
plt.figure(figsize=(10, 6))
plt.barh(keys, values, color='skyblue')
plt.xlabel('Number of Tweets')
plt.title(f"Top 10 for {args.key}")
plt.tight_layout()

# Detect if input is lang or country
file_type = 'lang' if 'lang' in args.input_path else 'country'

# Set output filename with suffix
output_filename = f"{args.key[1:]}.{file_type}.png"
plt.savefig(output_filename)
print(f"Plot saved as {output_filename}")

