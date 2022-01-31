x=int(input())
sizes=[0 for _ in range(17)]
size=list(map(int, input().split()))
for i in size:sizes[i-3]+=1
n=int(input())
total=0
for _ in range(n):
    pursize, purprice=map(int, input().split())
    if sizes[pursize-3]==0:continue
    total+=purprice
    sizes[pursize-3]-=1
print(total)