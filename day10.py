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

"""
(any time you see is the result of running the program 3 times and taking the median for 50 iterations)
my original answer took 8.3 seconds to get the solution
Implemented caching -> 7.3s
Changed from strings to lists -> 4.9s ----- since strings are immutable types in python, every time you "edit" a string, you are actually copying and replacing it. This isn't important 
                                            until you're editing large strings a lot of times (like right here!)

there are always ways to make improvements but I'm satisfied with what I've got here


"""

start = time.time()


def update_sequence(sequence):
    #break up the string based on when the next entry is different
    tokens = []
    i = 0
    last_num = sequence[0]
    counter = 1
    while i < len(sequence)-1:
        if sequence[i+1] == last_num:
            counter += 1
        else:
            tokens.append(int(counter))
            tokens.append(int(last_num))
            counter = 1
            last_num = sequence[i+1]

        i += 1

    tokens.append(int(counter))
    tokens.append(int(last_num))

    return tokens

sequence = list(file.readline())
file.close()


for i in range(50):
    sequence = update_sequence(sequence)

print(len(sequence))





end = time.time()
print(f"Runtime: {end-start}")