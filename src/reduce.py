#!/usr/bin/env python3

import argparse
import json
from collections import Counter, defaultdict

parser = argparse.ArgumentParser()
parser.add_argument('input_files', nargs='+', help='List of input .lang or .country files')
args = parser.parse_args()

combined_counts = defaultdict(Counter)

for file in args.input_files:
    with open(file, 'r') as f:
        data = json.load(f)
        for hashtag, counts in data.items():
            combined_counts[hashtag].update(counts)

print(json.dumps(combined_counts))
