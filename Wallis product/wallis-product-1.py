"""
Wallis product - Pi approximation
Simple algorithm
"""

from __future__ import division

# Pi first decimals (generated by Wolfram Mathematica)
pi = 3.141592653589793238462643383279

my_pi = 1

n = int(raw_input('How many product terms? '))

for j in range(1, n):
    my_pi *= 4 * j ** 2 / (4 * j ** 2 - 1)

my_pi *= 2

print pi
print my_pi
print abs(my_pi - pi)
