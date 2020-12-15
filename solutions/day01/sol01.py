def getSol():
    initialProblemInput = open("input01", "r").read().split("\n")
    del initialProblemInput[len(initialProblemInput)-1]
    problemInput = []

    for val in initialProblemInput:
        problemInput.append(int(val))

    solutions = {}

    for val1 in problemInput:
        for val2 in problemInput[problemInput.index(val1)+1:]:
            if val1+val2 == 2020:
                solutions["one"] = val1*val2
            else:
                for val3 in problemInput[problemInput.index(val2)+1:]:
                    if val1+val2+val3 == 2020:
                        solutions["two"] = val1*val2*val3
            if len(solutions) == 2:
                return solutions


solutions = getSol()

print("Solution 1 is {}, and Solution 2 is {}.".format(solutions["one"], solutions["two"]))

