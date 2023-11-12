numList = [] 
validList = []

def countInRange(low, high, numList):
    i = 0
    for i in numList:
        if (low) <= (i) <= (high):
            validList.append(i)
            print(i, "is valid")
        else:
            print(i, "is not valid")
    return validList

print(countInRange(5,7,[1,5,9,6,7,2,3,1,1]))
