5372. 주사위의 합
# -*- coding: utf-8 -*-
from sys import stdin
N=int(input())
for i in range(1,7):
    for j in range(1,7):
    
        if i+j==N:
            
            print(i,j)
