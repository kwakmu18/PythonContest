import sys
al=['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
def print_rangoli(size):
    for i in range(size):
        sys.stdout.write('-'*(2*(size-i-1)))
        index=size-1
        for _ in range(i):
            sys.stdout.write(al[index]+'-') 
            index-=1
        sys.stdout.write(al[index])
        if i!=0:sys.stdout.write('-')
        index+=1
        for _ in range(i):
            sys.stdout.write(al[index])
            if index!=size-1:sys.stdout.write('-')
            index+=1
        sys.stdout.write('-'*(2*(size-i-1))+"\n")

    for i in range(size-1,0,-1):
        index=size-1
        sys.stdout.write('-'*(2*(size-i)))
        for _ in range(i-1):
            sys.stdout.write(al[index]+'-')
            index-=1
        sys.stdout.write(al[index])
        if i!=1:sys.stdout.write('-')
        index+=1
        for _ in range(i-1):
            sys.stdout.write(al[index])
            if index!=size-1:sys.stdout.write('-')
            index+=1
        sys.stdout.write('-'*(2*(size-i))+"\n")
    

if __name__ == '__main__':
    n = int(input())
    print_rangoli(n)
