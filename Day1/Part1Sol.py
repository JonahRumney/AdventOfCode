import math

with open("input.txt", "r") as file:
    left = []
    right = []
    for line in file:
        line = line.strip().split("   ")
        print(line[0])
        print(line[1])
        left.append(int(line[0]))
        right.append(int(line[1]))

left.sort()
right.sort()
total = 0
for i in range(len(left)):
    total += abs(left[i] - right[i])
print(total) #2367773