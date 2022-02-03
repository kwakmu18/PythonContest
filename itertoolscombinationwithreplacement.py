from itertools import combinations_with_replacement
s,n=input().split()
l=list(combinations_with_replacement(s, int(n)))
for i in range(len(l)):
    l[i]=list(l[i])
    l[i].sort()
for i in sorted(l):
    print(''.join(i))