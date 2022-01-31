from itertools import product
import sys
a=input().split()
for i in range(len(a)):a[i]=int(a[i])
b=input().split()
for i in range(len(b)):b[i]=int(b[i])
print(a,b)
prod=list(product(a,b))
for i in prod:
    print(i,end=' ')