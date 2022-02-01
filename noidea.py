n,m=map(int, input().split())
array=input().split()
d={}
for i in array:
    try:d[i]+=1
    except KeyError:d[i]=1
seta=set(input().split())
setb=set(input().split())
happiness=0
for i in d:
    if i in seta:
        happiness+=int(d[i])
        seta.remove(i)
    elif i in setb:
        happiness-=int(d[i])
        setb.remove(i)
print(happiness)


# n,m=map(int, input().split())
# d={}
# array=input().split()
# for i in array:
#     try:
#         if d[i]==True:continue
#     except KeyError:d[i]=True
# seta=set(input().split())
# setb=set(input().split())
# happiness=0
# for i in seta:
#     try:
#         if d[i]:happiness+=1
#     except KeyError:continue
# for i in setb:
#     try:
#         if d[i]:happiness-=1
#     except KeyError:continue
# print(happiness)