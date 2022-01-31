if __name__ == '__main__':
    s = input()
    alphanumeric, alphabetic, digit, lower,upper=False,False,False,False,False
    for i in s:
        if i.isalnum():alphanumeric=True
        elif i.isalpha():alphabetic=True
        elif i.isdigit():digit=True
        elif i.islower():lower=True
        elif i.isupper():upper=True
    print(alphanumeric)
    print(alphabetic)
    print(digit)
    print(lower)
    print(upper)