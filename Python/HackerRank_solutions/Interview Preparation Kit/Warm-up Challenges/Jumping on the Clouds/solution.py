# https://www.hackerrank.com/challenges/jumping-on-the-clouds/problem

import math
import os
import random
import re
import sys


# Complete the jumpingOnClouds function below.
def jumpingOnClouds(c, n):
    jump = 0
    i = 0
    while i < n-1:
        if i + 2 < n and c[i + 2] == 0:
            i = i + 2
            jump += 1
        else:
            i = i + 1
            jump += 1
    return jump


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    c = list(map(int, input().rstrip().split()))

    result = jumpingOnClouds(c, n)

    fptr.write(str(result) + '\n')

    fptr.close()
