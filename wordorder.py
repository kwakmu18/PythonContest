from collections import OrderedDict
d=OrderedDict()
n=int(input())
for _ in range(n):
    s=input()
    try:d[s]+=1
    except KeyError:d[s]=1
print(len(d))
for i in d:print(d[i],end=' ')