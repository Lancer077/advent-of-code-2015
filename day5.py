
path = "input.txt"
file = open(path, "r")

#just going to write helper functions here
def is_nice(string: str):
    if vowel_check(string, 3) and consecutive_check(string) and bad_string_check(string):
        return True
    return False

def vowel_check(string: str, vowel_count: int):
    counter = 0
    for char in string:
        if char in ["a", "e", "i", "o", "u"]:
            counter += 1
    if counter >= vowel_count:
        return True
    return False

def consecutive_check(string: str):
    for i in range(len(string)-1):
        if string[i] == string[i+1]:
            return True
    return False

def bad_string_check(string: str):
    bad_strings = ["ab", "cd", "pq", "xy"]
    for bad_s in bad_strings:
        if bad_s in string:
            return False
    return True

def is_nice_2(string: str):
    if repeats_with_letter_between(string) and check_pairs(string):
        return True
    return False

def repeats_with_letter_between(string: str):
    for i in range(len(string)-2):
        if string[i] == string[i+2]:
            return True
    return False

def check_pairs(string: str):
    pairs = [] #(letter a, letter b, location of letter a)
    for i in range(len(string)-1):
        pairs.append((string[i], string[i+1], i))
    
    
    for i in range(len(pairs)):
        for j in range(i):
            if pairs[i][0] == pairs[j][0] and pairs[i][1] == pairs[j][1] and abs(pairs[i][2] - pairs[j][2]) > 1:
                return True
    return False
        

counter_1 = 0
counter_2 = 0
for line in file:
    if is_nice(line):
        counter_1 += 1
    if is_nice_2(line):
        counter_2 += 1

print(f"Part 1: {counter_1}")
print(f"part 2: {counter_2}")

