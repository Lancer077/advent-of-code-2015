import sys
import os
import time
import numpy
import re
import heapq
from collections import defaultdict, deque
from z3 import Int, Solver, sat
from functools import cache

path = "input.txt"
file = open(path, "r")

start = time.time()

def read_line(line):
    len1 = len(line)
    line = line[1:-1] #cut off the surrounding quotes

    len2 = 0
    i = 0
    while i < len(line):
        len2 += 1
        if line[i] == "\\":
            if line[i+1] == "\\" or line[i+1] == "\"":
                i += 1
            elif line[i+1] == "x":
                try:
                    int(line[i+2:i+3], 16)
                    i += 3
                except:
                    pass
        i += 1

    return len1-len2

def read_line_2(line):
    len1 = len(line)
    len2 = 0
    i = 0
    while i < len(line):
        len2 += 1
        if line[i] == "\"" or line[i] == "\\":
            len2 += 1
        i += 1

    len2 += 2

    return abs(len1-len2)


counter = 0
counter2 = 0
for line in file:
    counter += read_line(line)
    counter2 += read_line_2(line)

print(f"Part 1: {counter}")
print(f"Part 2: {counter2}")


end = time.time()
print(f"Runtime: {end-start}")