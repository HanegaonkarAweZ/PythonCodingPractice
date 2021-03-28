# -*- coding: utf-8 -*-
"""
Created on Sun Feb 14 09:10:18 2021

@author: DELL
"""

S = []

for i in range(0,10):
    for j in range(0,10):
        number = pow(2,i)*pow(3,j)
        S.append(number)

S.sort()
print(S[0:20])