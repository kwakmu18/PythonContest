n = int(input())
s = set(map(int, input().split()))
N=int(input())
for _ in range(N):
    S=input().split()
    if (len(S)==2):
        if S[0]=='remove': s.remove(int(S[1]))
        elif S[0]=='discard': s.discard(int(S[1]))
    else:s.pop()
print(sum(s))

