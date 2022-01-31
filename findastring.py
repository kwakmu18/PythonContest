def count_substring(string, sub_string):
    len1,len2,num=len(string),len(sub_string),0
    for i in range(0,len1-len2+1):
        flag=True
        for j in range(0,len2):
            if string[j+i]!=sub_string[j]:flag=False
        if flag:num+=1
    return num

if __name__ == '__main__':
    string = input().strip()
    sub_string = input().strip()
    
    count = count_substring(string, sub_string)
    print(count)