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

"""
First time trying the snippet feature of vs code to setup some imports and how I normally read in files
pretty neat, and you could really use it for pretty much anything
like if you had 20 common patterns already precoded there, a lot of this stuff would be breeze
if you wanted to always have quicksort at your disposal, you just need to code it once, and type the shortcut
it just seems really cool


"""

def read_line(line):
    tokens = line.split(" ")
    if "AND" in line: #always length 5
        pass
        #print(len(tokens))
    elif "RSHIFT" in line: #len 5
        pass
        #print(len(tokens))
    elif "OR" in line: # len 5
        #print(len(tokens))
        pass
    elif "LSHIFT" in line: # len 5
        pass
    elif "NOT" in line: # len 4
        pass
    else:
        print(len(tokens))

for line in file:
    read_line(line)




















end = time.time()
print(f"Runtime: {end-start}")
