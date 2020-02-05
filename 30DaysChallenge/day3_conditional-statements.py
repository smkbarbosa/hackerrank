#!/bin/python3

import math
import os
import random
import re
import sys


def findWheter(N):
    if N % 2 == 0:
        if N in range(2, 5):
            print('Not Weird')
        if N in range(6, 20):
            print('Weird')
        if N > 20:
            print('Not Weird')
    else:
        print('Weird')


if __name__ == '__main__':
    N = int(input())
    findWheter(N)
