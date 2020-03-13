# https://www.hackerrank.com/challenges/plus-minus/problem


#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the plusMinus function below.
def plusMinus(arr):
    zero = 0
    neg = 0
    pos = 0
    for i in range(0,n):
        if arr[i] < 0:
            neg += 1
        elif arr[i] > 0:
            pos += 1
        else:
            zero += 1
    print(pos / n)
    print(neg / n)
    print(zero / n)
if __name__ == '__main__':
    n = int(input())

    arr = list(map(int, input().rstrip().split()))

    plusMinus(arr)
