def mutate_string(string, position, character):
    strlist=list(string)
    strlist[position]=character
    string=''.join(strlist)
    return string

if __name__ == '__main__':
    s = input()
    i, c = input().split()
    s_new = mutate_string(s, int(i), c)
    print(s_new)