#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Apr 30 15:05:20 2019

@author: sangyy
"""
print ("学校操场的400米跑道中套着300米小跑道，大跑道与小跑道有200米路程相重，甲以每秒6米的速度沿大跑道逆时针方向跑，乙以每秒4米的速度沿小跑道顺时针方向跑，两人同时从两跑道的交点A处出发，当他们第二次在跑道上相遇时，甲共跑了多少米？")

n = input("请输入第几次相遇：");
n = int(n)
#甲乙走过的总里程
d = 0
for i in range(1,n+1):
    if i%9 == 1:
        d = d + 400
    else:
        d = d + 700
    
        
        
#相遇时甲走过距离
a = 6*(d/10)
#相遇时乙走过距离
b = 4*(d/10)

print ('第{}次相遇，甲乙走过的总里程是{}米，甲走过{}米,乙走过{}米'.format(n,d,a,b))