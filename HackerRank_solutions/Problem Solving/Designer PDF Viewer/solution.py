# https://www.hackerrank.com/challenges/designer-pdf-viewer/problem


#!/bin/python3

import math
import os
import random
import re
import sys


# Complete the designerPdfViewer function below.
def designerPdfViewer(h, word):
    maxletter = 0
    alphabet = list('abcdefghijklmnopqrstuvwxyz')
    for j in range(len(word)):
        i = alphabet.index(word[j])
        if h[i] > maxletter:
            maxletter = h[i]
    return maxletter * len(word)


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    h = list(map(int, input().rstrip().split()))

    word = input()

    result = designerPdfViewer(h, word)

    fptr.write(str(result) + '\n')

    fptr.close()
