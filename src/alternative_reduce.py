#!/usr/bin/env python3

import argparse
import json
import matplotlib.pyplot as plt
from collections import defaultdict
import os

parser = argparse.ArgumentParser()
parser.add_argument('--hashtags', nargs='+', required=True, help='List of hashtags to track')
args = parser.parse_args()

# Initialize data structure
hashtag_counts = {hashtag: [] for hashtag in args.hashtags}
dates = []

# Process each output file
for filename in sorted(os.listdir('outputs')):
    if filename.endswith('.lang'):
        date = filename.split('.')[0].replace('geoTwitter', '')
        dates.append(date)

        with open(os.path.join('outputs', filename), 'r') as f:
            data = json.load(f)

            for hashtag in args.hashtags:
                count = sum(data.get(hashtag, {}).values())
                hashtag_counts[hashtag].append(count)

# Plotting
plt.figure(figsize=(12, 6))
for hashtag, counts in hashtag_counts.items():
    plt.plot(dates, counts, label=hashtag)

plt.xlabel('Date')
plt.ylabel('Tweet Count')
plt.title('Hashtag Trends Over Time')
plt.xticks(rotation=45)
plt.legend()
plt.tight_layout()
plt.savefig('hashtag_trends.png')
print("Plot saved as hashtag_trends.png")
