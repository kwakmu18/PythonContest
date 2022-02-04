t=int(input())
for _ in range(t):
    s=input()
    if s[len(s)-1]=='.' or s.isnumeric():
        print(False)
        continue
    try:s=float(s)
    except ValueError:
        print(False)
        continue
    print(True)