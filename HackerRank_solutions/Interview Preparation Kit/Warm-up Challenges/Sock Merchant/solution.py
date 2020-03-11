# https://www.hackerrank.com/challenges/sock-merchant/problem

import math
import os
import random
import re
import sys

# Complete the countingValleys function below.


def countingValleys(n, s):
    i = 0
    s = s + ("#")
    count = 0
    valley = 0
    while i < n:
        if s[i] == "U":
            count = +1
            i = +1
        elif s[i] == "D":
            i = +1
            count = -1
            if count == -1:
                valley = +1

    return valley


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = 12

    s = ("DDUUDDUDUUUD")

    result = countingValleys(n, s)

    fptr.write(str(result) + '\n')

    fptr.close()
