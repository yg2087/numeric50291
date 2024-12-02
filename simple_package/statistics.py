###
## Module for basic statistics
###

## Here I need functions to take in data
## and do the following:
##
## 1. Calculate mean. Calculate median. Calculate 
##    standard deviation.
##
## 2. Display the result with a nice print statement.
##
## 3. Plot a histogram of the data, with the mean and median 
##    marked on the plot. This should be part of a new Python
##    file in the package, called graphics.py.
##
## 4. Remember to provide a mechanism for checking that the input
##    is a numpy array or a list (if a list, you must convert it
##    to a numpy array).
##
## 5. Also, do something and/or throw an exception/message if the
##    numpy and matplotlib packages are not installed.

import numpy as np
import matplotlib.pyplot as plt

user_input = input("Enter your data in a list format i.e [point1, point2, ...]")
user_list = list(map(int, user_input.split(',')))

data = np.array(user_list)


mean = np.mean(data)
standard_deviation = np.std(data)
median = np.median(data)



print("mean:", mean, 
      "standard deviation:", standard_deviation, 
      "median:", median)

from graphics import hist_plots
hist_plots(data, mean, median)

try:
    import numpy
    import matplotlib
except ImportError as e:
    raise ImportError(f"Required package is missing: {e.name}. Please install it using 'pip install {e.name}'")