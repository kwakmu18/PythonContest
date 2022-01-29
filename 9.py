def swap_case(s):
    ans=''
    for i in s:
        if i>='a' and i<='z':ans+=i.upper()
        elif i>='A' and i<='Z':ans+=i.lower()
        else:ans+=i
    return ans

if __name__ == '__main__':
    s = input()
    result = swap_case(s)
    print(result)