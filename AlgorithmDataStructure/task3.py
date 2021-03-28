# -*- coding: utf-8 -*-
"""
Created on Sun Feb 14 08:01:26 2021

@author: DELL
"""

N=100
products_of_powers_of_2and3 = []
power_of_2 = 1
while power_of_2 < N:
    product_of_powers_of_2and3 = power_of_2
    while product_of_powers_of_2and3 < N:
        products_of_powers_of_2and3.append(product_of_powers_of_2and3)
        product_of_powers_of_2and3 *= 3
    power_of_2 *= 2
products_of_powers_of_2and3.sort()
print(products_of_powers_of_2and3)