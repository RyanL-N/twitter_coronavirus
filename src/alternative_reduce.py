#!/usr/bin/env python3

import argparse
import json
import matplotlib.pyplot as plt
from collections import defaultdict
import os
from datetime import datetime

parser = argparse.ArgumentParser()
parser.add_argument('--hashtags', nargs='+', required=True, help='List of hashtags to track')
args = parser.parse_args()

# Initialize data structure
hashtag_counts = {hashtag: [] for hashtag in args.hashtags}
days_of_year = []

# Process each output file
for filename in sorted(os.listdir('outputs')):
    if filename.endswith('.lang'):
        date_str = filename.split('.')[0].replace('geoTwitter', '')  # Extract date (e.g., '20-01-01')

        # Convert to day of the year
        try:
            day_of_year = datetime.strptime(date_str, "%y-%m-%d").timetuple().tm_yday
            days_of_year.append(day_of_year)
        except ValueError:
            continue  # Skip files with invalid dates

        with open(os.path.join('outputs', filename), 'r') as f:
            data = json.load(f)

            for hashtag in args.hashtags:
                count = sum(data.get(hashtag, {}).values())
                hashtag_counts[hashtag].append(count)

# Plotting
plt.figure(figsize=(12, 6))
for hashtag, counts in hashtag_counts.items():
    plt.plot(days_of_year, counts, label=hashtag)

plt.xlabel('Day of the Year')
plt.ylabel('Tweet Count')
plt.title('Hashtag Trends Over Time')
plt.xticks(ticks=range(0, 366, 30), labels=[str(i) for i in range(0, 366, 30)])  # Show ticks every 30 days
plt.legend()
plt.grid(True, linestyle="--", alpha=0.5)
plt.tight_layout()
plt.savefig('hashtag_trends.png')
print("Plot saved as hashtag_trends.png")

