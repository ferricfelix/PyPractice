from collections import Counter
from math import sqrt
import sys


data = []

# Read in all data
with open(sys.argv[1], 'r') as f:
    for line in f:
        data.append(int(line))

# Calculate mean
N = len(data)
mean = sum(data)/N

# Calculate standard deviation
std_dev = sqrt(sum((x - mean)**2 for x in data)/(N - 1))

# Create a counter and determine the mode
c = Counter(data)
mode, _ = c.most_common(1)[0]

# Show results
print(f'Mean: {mean}')
print(f'Standard deviation: {std_dev}')
print(f'Mode: {mode}')
