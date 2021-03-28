# -*- coding: utf-8 -*-
"""
Created on Sun Mar 28 16:18:52 2021

@author: Awez

Metgod for finding gcd of two numbers

ex. gcd(8,16) is 8
"""

def gcdof(m,n):
    
    fm = []
    for i in range(1, m+1):
        if m%i == 0:
            fm.append(i)
            
    fn = []
    for i in range (1, n+1):
        if n%i ==0:
            fn.append(i)
            
    fc = []
    for f in fm:
        if f in fn:
            fc.append(f)
            
            
    return fc[-1]

print(gcdof(8, 46))