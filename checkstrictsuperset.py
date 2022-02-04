a=set(input().split())
b=set()
for i in range(int(input())):
    s=set(input().split())
    b.update(s)
if a.issuperset(b):print(True)
else:print(False)