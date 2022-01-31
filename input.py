x,n=map(int, input().split())
num=input().split('+')
ans=0
for i in num:
    i.replace('x', str(x))
    k=eval(i)
    ans+=k
if (ans==n): print("True")
else: print("False")