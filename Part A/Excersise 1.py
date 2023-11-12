def getTotal (dicVals):
    total = 0
    #
    for item in dicVals:
        total += dicVals[item] 
    #
    return total

print(getTotal({'A':3,'B':5,'C':2}))