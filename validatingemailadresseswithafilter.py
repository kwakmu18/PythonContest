import re
def fun(s):
    l=re.split("[@, \.]",s)
    print(len(l)!=3, len(l[2])>3,  l[1].isalnum()==False, l[2].isalpha()==False,  '' in l, '@' not in s, (l[0].replace('-','').isalnum()==False, l[0].replace('_','').isalnum()==False))
    if (len(l)!=3 or len(l[2])>3 or l[1].isalnum()==False or l[2].isalpha()==False or '' in l or '@' not in s or (l[0].replace('-','').isalnum()==False and l[0].replace('_','').isalnum()==False)):return False
    else:return True
    # return True if s is a valid email, else return False

def filter_mail(emails):
    return list(filter(fun, emails))

if __name__ == '__main__':
    n = int(input())
    emails = []
    for _ in range(n):
        emails.append(input())

filtered_emails = filter_mail(emails)
filtered_emails.sort()
print(filtered_emails)