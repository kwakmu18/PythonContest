n,x=map(int, input().split())
score=[0 for _ in range(n)]
for _ in range(x):
    s=list(map(float, input().split()))
    for i in range(n):score[i]+=s[i]
for i in score:print("%.1f"%(i/x))