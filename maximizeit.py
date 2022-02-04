import itertools

k,m=map(int, input().split())
moddedlist=[]
numarr=[]
for i in range(k):numarr.append(list(map(int, input().split()))[1:])
ans=list(itertools.product(*numarr))
for i in ans:moddedlist.append(sum(j**2 for j in i)%m)
print(max(moddedlist))