#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Aug 31 09:28:21 2019

@author: sangyy
"""
#何老师从编程描述真实场景的解题思路
tempA = range(400)
tempB = range(400,100,-1)
A = []
B = []
for a in tempA:
    A.append(a)
for b in tempB:
    B.append(b)
i = 0
while(i<len(A)):
    if A[i] < 200:
        A[i] = A[i] + 0.1
    i += 1
i = 0
while(i<len(B)):
    if B[i] < 200:
        B[i] = B[i] + 0.2
    i += 1


i = 0
Afinal = 0
Bfinal = 0
while(True):
    if i > 1000:
        break
    if A[(i*6)%400] == B[(i*4)%300]:
        print("time: "+str(i)+"s")
        print("A in "+str(A[(i*6)%400]))
        print("B in "+str(B[(i*4)%300]))
        print("A一共跑了："+str(Afinal))
        print("B一共跑了："+str(Bfinal))
    i += 1
    Afinal += 6
    Bfinal += 4
    

    


