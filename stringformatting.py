def print_formatted(number):
    width=len(bin(number)[2:])
    for i in range(1,number+1):
        o,h,b=oct(i)[2:], hex(i)[2:].upper(), bin(i)[2:]
        print(str(i).rjust(width)+o.rjust(width+1)+h.rjust(width+1)+b.rjust(width+1))

if __name__ == '__main__':
    n = int(input())
    print_formatted(n)


#마지막 수의 2진법 자리수를 기반으로.