# -*- coding: utf-8 -*-
"""
Created on Tue Dec  1 09:15:55 2020

@author: DELL
"""

import math

def solve(a,b,c):
    d=math.sqrt(b**2-4*a*c)
    x1=(-b-d)/(2*a)
    x2=(-b+d)/(2*a)
    return x1,x2  #returning multiple values

x1,x2=solve(1,3,-4)
print(x1)
print(x2)