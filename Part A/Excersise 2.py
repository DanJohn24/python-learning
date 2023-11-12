def normalise (dicVals):
    vals = dicVals

    total = 0

    for item in vals:
        total += vals[item]

    for item in vals:
        vals[item] = vals[item] / total
    
    return vals
 
print (normalise({'A':3,'B':5,'C':2}))