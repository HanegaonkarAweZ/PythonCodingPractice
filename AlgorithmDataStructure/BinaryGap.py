# -*- coding: utf-8 -*-
"""
Created on Sat Feb 13 11:10:47 2021

@author: DELL
"""

def maxZeros(N): 
  
    # variable to store the length  
    # of longest consecutive 0's 
    maxm = -1
  
    # to temporary store the  
    # consecutive 0's 
    cnt = 0
    N = bin(N).replace("0b", "")
    while(N): 
        if(not(N & 1)): 
            cnt += 1
            N >>= 1
            maxm = max(maxm,cnt) 
        else: 
            maxm = max(maxm,cnt) 
            cnt = 0
            N >>= 1
  
    return maxm 
  
# Driver Code 
N = 1041
print(maxZeros(N)) 