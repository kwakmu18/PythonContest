#!/bin/python3

if __name__ == '__main__':
    s=input()
    alpha=dict()
    for i in s:
        try:alpha[i]+=1
        except KeyError:alpha[i]=1
    alpha=sorted(alpha.items(), reverse=True, key=lambda x:(x[1], x[0]))
    ans=dict()
    for i in alpha:
        try:ans[i[1]].append(i[0])
        except KeyError:ans[i[1]]=[i[0]]
        cnt=0
    for i in ans.items():
        for j in sorted(i[1]):
            if cnt==3:break
            print(j, end=' ')
            print(i[0])
            cnt+=1