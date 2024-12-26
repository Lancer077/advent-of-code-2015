

path = "input.txt"
file = open(path, "r")

def get_line_coords(line):
    line = line.replace("toggle ", "")
    line = line.replace("turn off ", "")
    line = line.replace("turn on ", "")
    tokens = line.split(" through ")
    x1, y1 = tokens[0].split(",")
    x2, y2 = tokens[1].split(",")
    return int(x1), int(y1), int(x2), int(y2)

arr = [[False for _ in range(1000)] for _ in range(1000)]
arr2 = [[0 for _ in range(1000)] for _ in range(1000)]

def modify_arr(x1, y1, x2, y2, action, arr, part):
    cur_y = y1
    while cur_y <= y2:
        cur_x = x1
        while cur_x <= x2:
            if part == 1:
                if action == 0: #turn on
                    arr[cur_y][cur_x] = True
                elif action == 1: # turn off
                    arr[cur_y][cur_x] = False
                elif action == 2: #toggle
                    arr[cur_y][cur_x] = not arr[cur_y][cur_x]
            elif part == 2:
                if action == 0: #turn up
                    arr[cur_y][cur_x] += 1
                elif action == 1 and arr[cur_y][cur_x] != 0: # turn down
                    arr[cur_y][cur_x] -= 1
                elif action == 2: #turn up by 2
                    arr[cur_y][cur_x] += 2
            cur_x += 1
        cur_y += 1
    return arr


def count_lit_lights(arr):
    counter = 0
    for row in arr:
        for col in row:
            if col:
                counter += 1
    return counter

def count_brightness(arr):
    counter = 0
    for row in arr:
        for col in row:
            counter += col
    return counter




for line in file:
    x1, y1, x2, y2 = get_line_coords(line)
    if "toggle" in line:
        action = 2
    elif "turn off" in line:
        action = 1
    elif "turn on" in line:
        action = 0
    arr = modify_arr(x1, y1, x2, y2, action, arr, 1)
    arr2 = modify_arr(x1, y1, x2, y2, action, arr2, 2)

print(count_lit_lights(arr))
print(count_brightness(arr2))
