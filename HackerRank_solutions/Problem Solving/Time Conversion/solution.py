# https://www.hackerrank.com/challenges/cleaned-conversion/problem


import sys

def cleanedConversion(s):
    # Complete this function
    cleaned = ""

    if(s[-2:] == "PM"):
        if(int(s[0:2]) < 12):
            cleaned = cleaned + str(12 + int(s[0:2])) + s[2:-2]
        else:
            cleaned = cleaned + str(int(s[0:2])) + s[2:-2]
    else:
        if(s[0:2] == '12'):
            cleaned = cleaned + "00" + s[2:-2]
        else:
            cleaned = cleaned + s[:-2]

    return cleaned

s = input().strip()
result = cleanedConversion(s)
print(result)
