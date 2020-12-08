# https://www.hackerrank.com/challenges/migratory-birds/problem


#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the migratoryBirds function below.
def migratoryBirds(arr):

    type_freq = [0, 0, 0, 0, 0, 0]

    for i in range(len(arr)):

        type_freq[arr[i]] += 1

    return type_freq.index(max(bird_freq))

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    arr_count = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    result = migratoryBirds(arr)

    fptr.write(str(result) + '\n')

    fptr.close()
