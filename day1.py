path = "input.txt"
file = open(path, "r")

cur_floor = 0
instruction_counter = 0
found_basement = False

for line in file:
    for char in line:
        instruction_counter += 1
        if char == "(":
            cur_floor += 1
        elif char == ")":
            cur_floor -= 1

        if cur_floor == -1 and not found_basement:
            pos = instruction_counter
            found_basement = True

file.close()
print(f"Answer for part 1: {cur_floor}")
print(f"Answer for part 2: {pos}")