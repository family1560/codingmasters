# -*- coding: utf-8 -*-
import sys, decimal
input = sys.stdin.readline
p, q = map(int, input().split())
n = int(input())

context = decimal.getcontext()
context.prec = n + 1
print(round(decimal.Decimal(p) / decimal.Decimal(q), n))
