# https://www.hackerrank.com/challenges/breaking-best-and-worst-records/problem


# !/bin/python3

import math
import os
import random
import re
import sys


# Complete the breakingRecords function below.
def breakingRecords(scores):
    scr_max = int(scores[0])  # set maximum scrore equal to first entry
    countmax = 0
    scr_min = int(scores[0])  # set minimum scrore equal to first entry
    countmin = 0
    for i in range(n):
        if scores[i] < scr_min:
            countmin += 1
            scr_min = int(scores[i])
        elif scores[i] > scr_max:
            countmax += 1
            scr_max = int(scores[i])
    return countmax, countmin


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    scores = list(map(int, input().rstrip().split()))

    result = breakingRecords(scores)

    fptr.write(' '.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
