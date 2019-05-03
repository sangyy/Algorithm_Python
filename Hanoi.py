#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri May  3 15:14:04 2019

@author: sangyy
"""
count = 0
def hanoi(a,b,c,n):
    global count
    count += 1
    if n == 1:
        print(a,'->',c)
    else:
        hanoi(a,c,b,n-1)
        print(a,'->',c)
        hanoi(b,a,c,n-1)
    
hanoi('a','b','c',4)
print(count)