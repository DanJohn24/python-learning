def NonZero(dicVals):
    total = 0
    #
    for key, value in dicVals.items():
        if value != 0:
            print (key,":",value)
    
NonZero({'A':3,'B':5,'C':0,'D':2})

