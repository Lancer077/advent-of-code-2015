path = "input.txt"
file = open(path, "r")


def get_new_loc(dir, x, y):
    if dir == "v":
        return x, y+1
    elif dir == "<":
        return x-1, y
    elif dir == "^":
        return x, y-1
    elif dir == ">":
        return x+1, y


cur_x = cur_y = 0
cur_loc = (cur_x, cur_y)
visited = {}

visited[cur_loc] = 1
for line in file:
    for direction in line:
        cur_x, cur_y = get_new_loc(direction, cur_x, cur_y)
        cur_loc = (cur_x, cur_y)

        if cur_loc not in visited:
            visited[cur_loc] = 1

print(f"Part 1: {len(visited)}")
file.close()

file = open(path, "r")
cur_x = cur_y = rob_x = rob_y = 0
visited = {}
#add starting location
visited[(0,0)] = 1

santa_turn = True

for line in file:
        for dir in line:
            if santa_turn:
                cur_x, cur_y = get_new_loc(dir, cur_x, cur_y)
                cur_loc = (cur_x, cur_y)
            if not santa_turn:
                rob_x, rob_y = get_new_loc(dir, rob_x, rob_y)
                cur_loc = (cur_x, cur_y)
            visited[cur_loc] = 1
            santa_turn = not santa_turn

file.close()
print(f"Part 2: {len(visited)}")


