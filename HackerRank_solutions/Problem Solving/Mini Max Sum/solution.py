# https://www.hackerrank.com/challenges/mini-max-sum/problem


#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the miniMaxSum function below.
def miniMaxSum(arr):
    minList = sorted(arr)
    minList.pop()
    maxList = sorted(arr)
    maxList.reverse()
    maxList.pop()
    print(sum(minList), end = " ")
    print(sum(maxList))

if __name__ == '__main__':
    arr = list(map(int, input().rstrip().split()))

    miniMaxSum(arr)
