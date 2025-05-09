with open("input.txt", "r") as file:
    # want list of list
    levels = []
    for line in file:
        level = []
        parts = line.strip().split(" ")
        print(len(parts))
        i = 0
        while i < len(parts):
            level.append(int(parts[i]))
            i += 1
        levels.append(level)
    
print(levels)
# == is neither ascending nor decreasing
numSafe = 0
for level in levels:
    n = len(level)
    print(f"length of array: {n}")
    isAscending = True
    isDescending = True
    isValid = True
    for i in range(n-1): 
        if not (0 < abs(level[i] - level[i+1]) <= 3):
            isValid = False
            break
        elif level[i] >= level[i+1]:
            isAscending = False
        elif level[i] <= level[i+1]:
            isDescending = False
    if (isValid and (isAscending or isDescending)):
        numSafe += 1

print(numSafe)


    



