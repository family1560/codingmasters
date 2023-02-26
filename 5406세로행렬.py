import sys

n = int(input())
for i in range(n):
    for j in range(i+1, n**2+1, n):
        print(j, end = ' ')
    print()
