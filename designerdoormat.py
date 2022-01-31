if __name__=='__main__':
    n,m=map(int, input().split())
    for i in range(n//2,0,-1):
        print('-'*3*i + '.|.'*(2*(n//2-i)+1)+'-'*3*i)
    print('-'*((n-1)//2*3-2) + "WELCOME" + '-'*((n-1)//2*3-2))
    for i in range(1,n//2+1):
        print('-'*3*i + '.|.'*(2*(n//2-i)+1)+'-'*3*i)