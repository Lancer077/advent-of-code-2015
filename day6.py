"""
my original solution took 6 seconds
Nobody has that kind of time

After some refactoring I was able to get it to a bit over 3 seconds
I'm not fully satisfied but I'm happy enough

"""

import time
start = time.time()

path = "input.txt"
file = open(path, "r")

#prevented string manipulation here
def get_line_coords(line):
    tokens = line.split(" ")
    x1, y1 = tokens[-3].split(",")
    x2, y2 = tokens[-1].split(",")
    return int(x1), int(y1), int(x2), int(y2)



def loop_instructions(file):
    #t1 = time.time()


    arr1 = [[False for _ in range(1000)] for _ in range(1000)]
    arr2 = [[0 for _ in range(1000)] for _ in range(1000)]

    for line in file:
        #print(line)
        x1, y1, x2, y2 = get_line_coords(line)
        if line.startswith("tog"):
            action = 2
        elif line.startswith("turn of"):
            action = 1
        elif line.startswith("turn on"):
            action = 0

        cur_y = y1
        while cur_y <= y2:
            cur_x = x1
            while cur_x <= x2:
                match action:
                    case 0: #turn on
                        arr1[cur_y][cur_x] = True
                        arr2[cur_y][cur_x] += 1
                    case 1: #turn off
                        arr1[cur_y][cur_x] = False
                        if arr2[cur_y][cur_x] > 0:
                            arr2[cur_y][cur_x] -= 1
                    case 2: #toggle
                        arr1[cur_y][cur_x] = not arr1[cur_y][cur_x]
                        arr2[cur_y][cur_x] += 2
                cur_x += 1
            cur_y += 1

    #t2 = time.time()
    #print(f"Time taken to read input text and update arrays: {t2-t1}")

    part_1_ans = part_2_ans = 0

    for row in arr1:
        for col in row:
            if col:
                part_1_ans += 1

    for row in arr2:
        for col in row:
            part_2_ans += col

    print(f"Answer for part 1: {part_1_ans}")
    print(f"Answer for part 2: {part_2_ans}")


loop_instructions(file)


end = time.time()
print(f"time taken: {end-start}")
