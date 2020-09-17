import re

def fun(s):
    # return True if s is a valid email, else return False
    regex = ("^\w+([\.-]?\w+)*@\w+([\.-]?\w+)*(\.\w{2,3})+$")

    if(re.search(regex,s)):
        return True
    else:
        return False


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
