# https://www.hackerrank.com/challenges/repeated-string/problem

# !/bin/python3

import os


# Complete the repeatedString function below.
def repeatedString(s, n):
    len_str = len(s)
    num_str = (n // len_str)
    remainder = (n % len_str)
    count1 = count2 = 0

    for i in range(len_str):
        if s[i] == "a":
            count1 += 1
        if s[i] == "a" and (i < remainder):
            count2 += 1
    total = count1 * num_str + count2
    return total


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    n = int(input())

    result = repeatedString(s, n)

    fptr.write(str(result) + '\n')

    fptr.close()
