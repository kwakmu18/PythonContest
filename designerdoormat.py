if __name__=='__main__':
    n,m=map(int, input().split())
    for i in range(n//2,0,-1):
        print('-'*3*i + '.|.'*(2*(n//2-i)+1)+'-'*3*i)
    print('-'*((n-1)//2*3-2) + "WELCOME" + '-'*((n-1)//2*3-2))
    for i in range(1,n//2+1):
        print('-'*3*i + '.|.'*(2*(n//2-i)+1)+'-'*3*i)

# (2k+1) : (3k) times of '-'
# 3 : 3 times
# 5 : 6 times
# 7 : 9 times
# 9 : 12 times
# 11 : 15 times

# (2k+1) : (3k-2) times of '-'
# 7 : 7 times
# 9 : 10 times
# 11 : 13 times