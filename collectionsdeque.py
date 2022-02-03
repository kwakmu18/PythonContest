from collections import deque
d=deque()
n=int(input())
for _ in range(n):
    s=input().split()
    if s[0]=='append':d.append(int(s[1]))
    elif s[0]=='appendleft':d.appendleft(int(s[1]))
    elif s[0]=='pop':d.pop()
    else:d.popleft()
for i in d:
    print(i, end=' ')