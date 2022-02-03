from itertools import groupby
s=input()
for i,j in groupby(s):print("(%d, %d)"%(len(list(j)), int(i)), end=' ')