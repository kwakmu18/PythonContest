import itertools
inp=input().split()
allist=list(itertools.permutations(inp[0],int(inp[1])))
anslist=[]
for i in allist:
    s=""
    for j in i:s+=j
    anslist.append(s)
anslist=sorted(anslist)
for i in anslist:print(i)
