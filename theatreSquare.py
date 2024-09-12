"""
theatre square in the capital city of berland has a rectangular shape 
with the size "m x n". we have to flagstone this area and flagstones 
area is a x a.

find the least number of flagstones needed to pave the quare.
"""
import math
n, m, a = map(int, input().split())

fa = math.ceil(n / a)
fb = math.ceil(m / a)

total = fa * fb
print(total)
