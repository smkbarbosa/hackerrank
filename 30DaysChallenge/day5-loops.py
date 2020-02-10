#!/bin/python3

import math
import os
import random
import re
import sys


def loop_session(n):
  for i in range(1,11):
    result = n * i
    print(str(n) + ' x ' + str(i) + ' = ' + str(result) )


if __name__ == '__main__':
    n = int(input())
    loop_session(n);
