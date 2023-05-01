#!/usr/bin/env python

import sys
import csv

if len(sys.argv) < 2:
    print("Usage: python count_csv_columns.py <filename>")
    sys.exit(1)

filename = sys.argv[1]

counts = {}

with open(filename, newline='') as csvfile:
    reader = csv.reader(csvfile)
    for row in reader:
        num_cols = len(row)
        if num_cols not in counts:
            counts[num_cols] = 1
        else:
            counts[num_cols] += 1

for num_cols, count in counts.items():
    print(f"{num_cols} columns: {count} lines")
