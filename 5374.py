# -*- coding: utf-8 -*-
import sys

a,b=map(int,input().split())
if b-30<0:
    if a==0:
        a+=23
    else:
        a-=1
    b+=30
    print(a,b,end=' ')
else:
    print(a,b-30,end=' ')
print()
