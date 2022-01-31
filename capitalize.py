#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the solve function below.
def solve(s):
    a=s.split(' ')
    for i in range(len(a)):
        a[i]=a[i].capitalize()
    return ' '.join(a)
if __name__ == '__main__':
    fptr = open(os.environ['E:\git\PythonContest'], 'w')
    s = input()
    result = solve(s)
    print(result)
    fptr.write(result + '\n')
    fptr.close()
