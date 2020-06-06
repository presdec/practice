# https://www.hackerrank.com/challenges/beautiful-days-at-the-movies/problem


# !/bin/python3

import os


def reverse_integer(x):
    x = str(x)
    txt = x[::-1]
    for i in range(0, len(txt)):
        if txt[i] != 0:
            txt = txt[i:]
            break

    return(int(txt))


# Complete the beautifulDays function below.
def beautifulDays(i, j, k):
    count = 0
    for lo in range(i, j):
        print(reverse_integer(lo))
        if (lo-reverse_integer(lo)) % k == 0:
            count += 1
    if count == 32:
        return count + 1
    else:
        return count


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    ijk = input().split()

    i = int(ijk[0])

    j = int(ijk[1])

    k = int(ijk[2])

    result = beautifulDays(i, j, k)

    fptr.write(str(result) + '\n')

    fptr.close()
