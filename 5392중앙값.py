import sys

def solution(array):
    center=0
    idx=0
    a=sorted(array)
    
    if len(a)%2==1:
        idx=len(a)//2
        median=a[idx]
    return median
    
list=[]
a,b,c,d,e= map(int,input().split(" "))
list.append(a)
list.append(b)
list.append(c)
list.append(d)
list.append(e)

print(solution(list)) 
