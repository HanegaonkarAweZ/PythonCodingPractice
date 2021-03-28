# -*- coding: utf-8 -*-
"""
Created on Sun Mar 28 16:18:52 2021

@author: Awez

Metgod for finding gcd of two numbers

ex. gcd(8,16) is 8
"""

def gcd_a(m,n):
    
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

print(gcd_a(14, 63))


# Improvement to the above code

def gcd_b(m,n):
    fc = []
    for i in range(1, min(m,n) + 1):
        if (m%i == 0 and n%i == 0):
            fc.append(i)
            
    return fc[-1]

print(gcd_b(14,63))


# working from backward 


def gcd_c(m,n):
    i = min(m,n)
    
    while i>0:
        if (m%i == 0 and n%i ==0):
            return i
        else:
            i = i-1
            
print(gcd_c(14,63))


# more advance algorithm is using recursion

def gcd_d(m,n):
    
    if m<n:
        (m,n) = (n,m)
        
    if (m%n == 0):
        return n
    else:
        diff = m-n
        return gcd_d(max(n,diff), min(n,diff))
    
print(gcd_d(14,63))
    

def gcd_e(m,n):
    
    if m<n:
        (m,n) = (n,m)
        
    if m%n ==0:
        return n
    else:
        return gcd_e(n, m%n)
    
    
print(gcd_e(32,84))


def gcd_f(m,n):
    
    if m<n:
        (m,n) = (n,m)
        
    while m%n != 0:
        (m,n) = (n, m%n)
        
    return n

print(gcd_f(32,84))
        