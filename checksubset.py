t=int(input())
for _ in range(t):
    n=input()
    s1=set(input().split())
    m=input()
    s2=set(input().split())
    if len(s1.difference(s2))==0:print("True")
    else:print("False")