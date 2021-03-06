"""
Wallis product - Pi approximation
Better algorithm
It uses less division operations,
and thus minimizes rounding errors
"""

from __future__ import division

# Pi first decimals (generated by Wolfram Mathematica)
pi = 3.141592653589793238462643383279

n = int(raw_input('How many product terms? '))

num = 1
den = 1
for i in range(1, n):
    tmp = 4 * i * i
    num *= tmp
    den *= tmp - 1

better_pi = 2 * (num / den)

print pi
print better_pi
print abs(pi - better_pi)
