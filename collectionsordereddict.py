m=int(input())
mset=set(input().split())
n=int(input())
nset=set(input().split())
newset=list((mset-nset).union(nset-mset)-mset.intersection(nset))
newset.sort(key=int)
for i in newset:
    print(int(i))