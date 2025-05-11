import re


with open("input.txt", "r") as file:
        data = file.read()
        total = 0
        canMult = True
        # scans in left-to-right order, preserves order of appearance
        # match whichever appears next
        for x in re.finditer(r"do\(\)|don\'t\(\)|mul\((\d{1,3}),(\d{1,3})\)", data):
            match x[0]:
                case 'do()':
                    canMult = True
                case 'don\'t()':
                    canMult = False
                case _:
                    if canMult: 
                        total += int(x[1]) * int(x[2])
print(total) #93465710
    