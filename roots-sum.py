# File: roots-sums
# Name: Shiyue Li (shiyue.li[at]yale.edu)
# Date: June 16, 2017

from math import *
import numpy as np
import matplotlib.pyplot as plt

def roots_sum(n):
    """return the sum of k-th roots of a natural number n,
    k ranging from 2 to n."""
    return sum([np.power(n, (1.0/k)) for k in xrange(2, n+1)])

# later project, try calculate using Riemann L function

def plot(x, y):
    plt.plot(x, y)
    plt.xlabel("Natual Numbers")
    plt.ylabel("Sum of Roots")
    plt.axis([0, 1000, 0, 1200])
    plt.show()

def main():
    num = input('Enter a number greater than 2:')
    xy_values = [(x, roots_sum(x)) for x in xrange(2, num+1)]
    x_values = xrange(2, num+1)
    y_values = [xy[1] for xy in xy_values]

    ## Print out values in log for sanity check
    for (x, y) in xy_values:
        print "x:", x, "roots sum:", y

    ## Plot
    plot(x_values, y_values)

if __name__ == "__main__": main()
