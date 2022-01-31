import textwrap

def wrap(string, max_width):
    sl=textwrap.wrap(string, width=max_width) #왜 vscode에서는 안됨?
    return '\n'.join(sl)
if __name__ == '__main__':
    string, max_width = input(), int(input())
    result = wrap(string, max_width)
    print(result)