
def minion_game(string):
    slen=len(string)
    stuart, kevin=0, 0
    sword, kword=set(), set()
    for i in range(0,slen):
        if s[i]=='A' or s[i]=='I' or s[i]=='E' or s[i]=='O' or s[i]=='U':
            for j in range(i, slen):kword.add(string[i:j+1])
        else:
            for j in range(i, slen):sword.add(string[i:j+1])
    for i in sword:
        ilen=len(i)
        for j in range(0,slen-ilen+1):
            flag=True
            for k in range(j,j+ilen):
                if string[k]!=i[k-j]:flag=False
            if flag:
                stuart+=1
                print(i)
    for i in kword:
        ilen=len(i)
        for j in range(0,slen-ilen+1):
            flag=True
            for k in range(j,j+ilen):
                if string[k]!=i[k-j]:flag=False
            if flag:
                kevin+=1
                print(i)
    print("Stuart %d"%(stuart) if stuart>kevin else "Draw" if (stuart==kevin) else "Kevin %d"%(kevin))




if __name__ == '__main__':
    s = input()
    minion_game(s)