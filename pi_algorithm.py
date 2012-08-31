# -*- coding: utf-8 -*-
"""
Pi can be estimated using the function 4 * (1 – 1/3 + 1/5 – 1/7 + …) with more terms
giving greater accuracy.
This is a function that calculates Pi to an accuracy of 5 decimal
places

"""

denominator = 3
inner_algorithm = 1.0
sign = -1

while inner_algorithm > (3.14165 / 4) or inner_algorithm < (3.14155 / 4):
    inner_algorithm += (sign * (1.0 / denominator))
    denominator += 2
    sign *= -1
    
print inner_algorithm * 4