from collections import defaultdict
import sys
def print_list(a):
    for i in a:sys.stdout.write(str(i)+" ")
    print()
d=defaultdict(list)
a,b=map(int, input().split())
for i in range(1,a+1):
    s=input()
    if d[s]==[]:d[s]=[i]
    else:d[s].append(i)
for _ in range(b):
    s=input()
    if d[s]==[]:print(-1)
    else:print_list(d[s])