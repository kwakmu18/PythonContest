n=int(input())
columnname=input().split()
for i in range(4):
    if columnname[i]=='MARKS':markindex=i
totscore=0
for _ in range(n):
    scores=input().split()
    totscore+=int(scores[markindex])
print("%.2f"%(totscore/n))