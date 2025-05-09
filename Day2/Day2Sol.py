with open("input.txt", "r") as file:
    # want list of list
    reports = []
    for line in file:
        report = []
        parts = line.strip().split(" ")
        i = 0
        while i < len(parts):
            report.append(int(parts[i]))
            i += 1
        reports.append(report)
    
# == is neither ascending nor decreasing
numSafe = 0
safeReports = []
unsafeReports = []
for report in reports:
    n = len(report)
    isAscending = True
    isDescending = True
    isValid = True
    for i in range(n-1): 
        if not (0 < abs(report[i] - report[i+1]) <= 3):
            isValid = False
            break
        elif report[i] >= report[i+1]:
            isAscending = False
        elif report[i] <= report[i+1]:
            isDescending = False
    if (isValid and (isAscending or isDescending)):
        numSafe += 1
        safeReports.append(report)
    else: unsafeReports.append(report)
#PART 1 SOL = 257
print(numSafe)

# go through unsafe levels remove one element, and check for safety, if safe add to numSafe
# could make above safety check into function but will refactor later

for report in unsafeReports:
    print(f"unsafe level: {report}")
    #iterate through indices
    for i in range(len(report)):
        # BUG EX: if [1,2,3,4] remove 1 [2,3,4] then remove 2 [3,4] but want [1,3,4] make copy?
        #print(f"value to remove: {value}")
        # FIX: makes copy of array so we get above functionality
        modifiedReport = report[:i] + report[i+1:]
        n = len(modifiedReport)
        print(f"report with index {i} removed: {modifiedReport}")
        print(f"new length: {n}")
        isAscending = True
        isDescending = True
        isValid = True
        for i in range(n-1): 
            if not (0 < abs(modifiedReport[i] - modifiedReport[i+1]) <= 3):
                isValid = False
                break
            elif modifiedReport[i] >= modifiedReport[i+1]:
                isAscending = False
            elif modifiedReport[i] <= modifiedReport[i+1]:
                isDescending = False
        if (isValid and (isAscending or isDescending)):
            #print(f"{level} is now safe after removing {value}")
            numSafe += 1
            break
# PART 2 SOL = 328
print(numSafe) 


    



