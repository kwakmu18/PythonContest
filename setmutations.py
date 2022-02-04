n=input()
s1=set(map(int, input().split()))
m=int(input())
for i in range(m):
    a,b=input().split()
    s2=set(map(int, input().split()))
    eval("s1.%s(s2)"%(a))
print(sum(s1))