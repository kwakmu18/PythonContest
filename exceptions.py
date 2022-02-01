n=int(input())
for _ in range(n):
    a,b=input().split()
    try:print(int(a)//int(b))
    except ZeroDivisionError:
        print("Error Code: integer division or modulo by zero")
    except ValueError as a: print("Error Code: "+str(a))
    except ValueError as b: print("Error Code: "+str(b))