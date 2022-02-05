import re
s=input()
m=re.search(r'([a-zA-Z0-9])\1', s) #\1 is the replacement to use in case of a match, so a repeated word will be replaced by a single word.
print(m.group(1) if m else -1)