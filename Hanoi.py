#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri May  3 15:14:04 2019

@author: sangyy
"""
count = 0
def hanoi(a,b,c,n):
    global count
    
    if n == 1:
        count += 1
        print('第',count,'次移动:',a,'->',c)
    else:
        #把A柱上n-1个圆盘借助C柱移动到B柱上
        hanoi(a,c,b,n-1)
        #把A柱上最大的圆盘移动到C柱上
        hanoi(a,b,c,1)
        #把B柱上n-1个圆盘借助A柱移动到C柱上
        hanoi(b,a,c,n-1)
num = int(input('请输入汉诺塔的圆盘数量:'))    
hanoi('a','b','c',num)
print("完成任务需要移动{}步。".format(count))