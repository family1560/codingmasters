
# -*- coding: utf-8 -*-
import sys

n=int(input())
if n%10==0:
    a=n//50000
    b=n%50000
    c=b//10000
    d=b%10000
    e=d//5000
    f=d%5000
    g=f//1000
    h=f%1000
    i=h//500
    j=h%500
    k=j//100
    l=j%100
    m=l//50
    n=l%50
    o=n//10
    p=n%10
    print(a + c + e + g + i + k + m + o)
