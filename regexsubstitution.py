import re
n=int(input())
for _ in range(n):
    s=input()
    ms=re.sub(r'(?<= )(\&\&|\|\|)(?= )', (lambda m: 'and' if m.group(1) == '&&' else 'or'), s)
    print(ms) 