import itertools
inp=input().split()
oup=list(itertools.combinations(inp[0],1))
for i in range(2,int(inp[1])+1):
    oup.extend(list(itertools.combinations(inp[0],i)))
anslist=[]
for i in oup:
    s=''.join(i)
    anslist.append([s, len(s)])

for i in sorted(anslist, key=lambda x:(x[1], x[0])):print(i[0])