#Exercise 1
def getTotal (dicVals):
    total = 0
    #
    for item in dicVals:
        total += dicVals[item] 
    #
    return total

'''
print(getTotal({'A':3,'B':5,'C':2}))
'''

#Excersise 2
def normalise (dicVals):
    vals = dicVals

    total = 0

    for item in vals:
        total += vals[item]

    for item in vals:
        vals[item] = vals[item] / total
    
    return vals

'''
print(normalise({'A':3,'B':5,'C':2}))
'''

#Excersise 3
def nonZero(dicVals):
    total = 0
    #
    for key, value in dicVals.items():
        if value != 0:
            print (key,":",value)

'''
nonZero({'A':3,'B':5,'C':0,'D':2})
'''

#Excersise 4
def analyse(votes,seats):
    for key, value in votes.items():
        voteOutput = round((value / getTotal(votes)) * 100)
        seatOutput = round((seats[key] / getTotal(seats)) * 100)
        #
        if voteOutput != 0 and seatOutput != 0:
            print (key, "has", voteOutput, "%","of the votes Vs.", seatOutput, "%","of the seats")

'''
votes = {'A':112,'B':52,'C':2,'D':36}
seats = {'A':3,'B':1,'C':0,'D':1}

analyse(votes,seats)
'''

#Excersise 5
def addTo(dic1, dic2):
    dict1Copy = dic1.copy()
    dict2Copy = dic2.copy()
    #
    for key,value in dic1.items():
        if key in dic2:
            foreignKey = dic2.get(key)
            foreignVal = dic2[key]
            #
            dict2Copy.pop(key)
            dict1Copy[key] = foreignVal + value
        #
    dict1Copy.update(dict2Copy)
    return (dict1Copy)

'''
myd1 = {'A':3,'B':1,'C':6,'D':1}
myd2 = {'X':5,'A':1,'Y':3,'D':7}

print(addTo(myd1,myd2))
'''