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
print(left)
print(right)
total = 0
for i in range(len(left)):
    occurences = 0
    for j in range(len(right)):
        if left[i] == right[j]:
            print("match")
            occurences += 1
    val = left[i] * occurences 
    print(f"{left[i]} appears {occurences} times")
    total += val

print(total) #21271939