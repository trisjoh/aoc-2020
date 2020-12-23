def getSol():
    problemInput = open("input02", "r").read().split("\n")
    del problemInput[len(problemInput)-1]
    checkList = []
    answer = [0, 0]
    
    for val in problemInput:
         firstSplit = val.split(" ")
         secondSplit = firstSplit[0].split("-")
         checkList.append([int(secondSplit[0]), int(secondSplit[1]), firstSplit[1], firstSplit[2]])
    
    for val in checkList:
        count = val[3].count(val[2][0])
        if count >= val[0] and count <= val[1]:
            answer[0] += 1
        if bool(val[3][val[0]-1] == val[2][0]) != bool(val[3][val[1]-1] == val[2][0]):
            answer[1] += 1

    return answer

answer = getSol()
print("The first answer is {}, and the second is {}.".format(answer[0], answer[1]))
