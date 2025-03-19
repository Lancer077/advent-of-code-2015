import sys
import os
import time
import numpy
import re
import heapq
from collections import defaultdict, deque
from z3 import Int, Solver, sat
from functools import cache

start = time.time()

path = "input.txt"
file = open(path, "r")

"""

"""

def build_map(file):
    routes = []
    locations = set()  #shoutout to sets, absolute goated data structure
    for line in file:
        line = line.replace("\n", "")
        tokens = line.split(" ")
        route = (tokens[0], tokens[2], int(tokens[4]))
        routes.append(route)
        locations.add(tokens[0])
        locations.add(tokens[2])
    routes = sorted(routes, key=lambda tup: tup[2])
    file.close()
    return locations, routes

def get_relevant_routes_1(location, visited, routes):
    relevant_routes = []
    for route in routes:
        if route[0] == location and route[1] not in visited:
            relevant_routes.append((route[1], route[2]))
        elif route[1] == locations and route[0] not in visited:
            relevant_routes.append((route[0], route[2]))
    return relevant_routes


def recursive_search(cur_loc, visited, locations, routes, cur_cost, min_cost):
    if cur_cost > min_cost or visited == locations:
        return cur_cost
    
    print(cur_cost)
    
    relevant_routes = get_relevant_routes_1(cur_loc, visited, routes)

    for route in relevant_routes:
        print(route)
        visited.add(cur_loc)
        cur_cost += route[1]
        cur_cost = recursive_search(route[0], visited, locations, routes, cur_cost, min_cost)
        print(cur_cost)
        #min_cost = min(cur_cost, min_cost)
        visited.discard(cur_loc)
        cur_cost -= route[1]





def find_min_path(locations, routes):
    min_cost = 1000000
    for l in locations:
        visited = set()
        recursive_search(l, visited, locations, routes, 0, min_cost)

    print(min_cost)



locations, routes = build_map(file)
print(locations)
find_min_path(locations, routes)






end = time.time()
print(f"Runtime: {end-start}")