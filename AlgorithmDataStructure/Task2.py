# -*- coding: utf-8 -*-
"""
Created on Sun Feb 14 07:34:02 2021

@author: DELL
"""
def maxOfString(S):
    finalSol = []
    N = len(S)-1
    for i in range(0,N):
        finalSol.append(S[i:i+2])
        
    return max((finalSol))
        
S = ""
print(maxOfString(S))