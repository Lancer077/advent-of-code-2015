path = "input.txt"
file = open(path, "r")

running_total = 0
ribbon = 0

for line in file:
    l, w, h = line.split("x")
    l, w, h = int(l), int(w), int(h)
    min_len = min(l*w, w*h, h*l)
    cur_total = (2*l*w) + (2*l*h) + (2*w*h) + min_len
    running_total += cur_total

    min_ribbon_len = min(2*(l+w), 2*(w+h), 2*(h+l))
    ribbon += min_ribbon_len + (l * w * h)



print(running_total)
print(ribbon)