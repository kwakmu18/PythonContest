import re
s=input()
m=re.findall(r'([AIEOUaieou]{2,})[^aieouAIEOU]', s)
if len(m)==0:print(-1)
else: 
    for i in m:print(i)