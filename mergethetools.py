import textwrap
def merge_the_tools(string, k):
    words=textwrap.wrap(string,k)
    for i in range(len(words)):
        words[i]=list(words[i])
        s=""
        for j in words[i]:
            if j in s:continue
            s+=j
        print(s)

if __name__ == '__main__':
    string, k = input(), int(input())
    merge_the_tools(string, k)