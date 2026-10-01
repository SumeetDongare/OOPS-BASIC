import pandas as pd
import numpy as np

# Create a Series containing 10 random numbers
s = pd.Series(np.random.randint(1, 100, 10))

print("Series:")
print(s)

# Indexing
print("\nFirst element:")
print(s[0])

# Filtering
print("\nNumbers greater than 50:")
print(s[s > 50])

# Statistical operations
print("\nMean:", s.mean())
print("Median:", s.median())
print("Minimum:", s.min())
print("Maximum:", s.max())


"""
OUTPUT:-
Series:
0     4
1    79
2    47
3    31
4    43
5    67
6    15
7    89
8    47
9    19
dtype: int32

First element:
4

Numbers greater than 50:
1    79
5    67
7    89
dtype: int32

Mean: 44.1
Median: 45.0
Minimum: 4
Maximum: 89
"""