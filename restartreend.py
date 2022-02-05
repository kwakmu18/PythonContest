import re
s=input()
k=input()
m=re.search(r'[%s]{1,1}'%(k), s)
n=re.findall(k, s)
print(m.start(), m.end())
print(n)