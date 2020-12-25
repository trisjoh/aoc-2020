def getSol():
    problemInput = open("input04", "r").read().split("\n") 
    breakpoints = []
    counter = 0
    sum = 0

    for val in problemInput:
        if val == "":
            breakpoints.append(counter)
        counter += 1

    for val in breakpoints:
        fieldcheck = 0
        if val == 2:
            sum += 1
        else: 
            for i in range(breakpoints[breakpoints.index(val)-1]+1, val):
                fieldcheck += problemInput[i].count("byr")
                fieldcheck += problemInput[i].count("iyr")
                fieldcheck += problemInput[i].count("eyr")
                fieldcheck += problemInput[i].count("hgt")
                fieldcheck += problemInput[i].count("hcl")
                fieldcheck += problemInput[i].count("ecl")
                fieldcheck += problemInput[i].count("pid")
        if (fieldcheck == 7):
            sum += 1
    
    return sum

print(getSol())





