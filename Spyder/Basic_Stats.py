# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

import numpy as np

# sample data set
data = [23,45,2,6,32,67,23,56,33,56,22,77,55,22]

# calculate mean
mean = np.mean(data)

# calculate median
median = np.median(data)

# print results
print(f"data: {data}")
print(f"mean: {mean}")
print(f"median: {median}")