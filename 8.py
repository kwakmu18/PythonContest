if __name__ == '__main__':
    N = int(input())
    num=[]
    for _ in range(N):
        s=input().split()
        if s[0]=="insert":
            num.insert(int(s[1]),int(s[2]))
        elif s[0]=="print":print(num)
        elif s[0]=="remove":
            num.remove(int(s[1]))
        elif s[0]=="append":
            num.append(int(s[1]))
        elif s[0]=="sort":num=sorted(num)
        elif s[0]=="pop":num.pop()
        elif s[0]=="reverse":num.reverse()

        