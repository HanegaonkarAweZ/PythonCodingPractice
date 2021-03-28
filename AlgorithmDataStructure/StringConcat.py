# -*- coding: utf-8 -*-
"""
Created on Sun Feb 14 07:08:33 2021

@author: DELL
"""

def stringConcat(name, surname, age):
    
    if (len(name)>1 and len(surname)>1 and age > 0):
        
        FinalString = name[0:2] + surname[0:2] + str(age)
        
        return FinalString
    else:
        return
    
name = "J0"
surname = "Aw"
age = 1
print(stringConcat(name,surname, age))