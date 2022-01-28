lowercase, uppercase, odd, even=[],[],[],[]
s=input()
for i in s:
    if i>='a' and i<='z':lowercase.append(i)
    elif i>='A' and i<='Z':uppercase.append(i)
    elif i>='0' and i<='9':
        if int(i)%2==0:even.append(i)
        else:odd.append(i)
print(''.join(sorted(lowercase))+''.join(sorted(uppercase))+''.join(sorted(odd))+''.join(sorted(even)))