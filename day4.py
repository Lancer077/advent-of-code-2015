import hashlib

path = "input.txt"
file = open(path)

for line in file:
    secret_key = line

file.close()

def solve(secret_key, zero_count):
    counter = 0
    while True:
        puzzle_input = secret_key
        puzzle_input += str(counter)

        result = (hashlib.md5(puzzle_input.encode()))

        result = result.hexdigest()

        if result[0:zero_count] == "0" * zero_count:
            break
        counter += 1
    return counter

part1 = solve(secret_key, 5)
print(f"Part 1: {part1}")

part2 = solve(secret_key, 6)
print(f"Part 2: {part2}")