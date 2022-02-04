from itertools import combinations
n=int(input())
aindex=[]
alpha=input().split()
for i in range(len(alpha)):
    if alpha[i]=='a':aindex.append(i+1)
k=int(input())
num=list(combinations([i for i in range(1,n+1)], k))
cnt=0
for i in num:
    for j in i:
        if j in aindex:
            cnt+=1
            break
print("%.4f"%(cnt/len(num)))
