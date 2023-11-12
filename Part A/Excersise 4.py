def NonZero(dicVals):
    vals = dicVals
    #
    total = 0
    #
    for key, value in vals.items():
        if value != 0:
            print (key,":",value)

def getTotal (dicVals):
    total = 0
    #
    for item in dicVals:
        total += dicVals[item] 
    #
    return total

def analyse(votes,seats):
    #votes portion
    for key, value in votes.items():
        name = key
        voteOutput = round((value / getTotal(votes)) * 100)
        seatOutput = round((seats[key] / getTotal(seats)) * 100)
        #
        if voteOutput != 0 and seatOutput != 0:
            print (name, "has", voteOutput, "%","of the votes Vs.", seatOutput, "%","of the seats")
               
votesDic = {'A':112,'B':52,'C':2,'D':36}
seatsDic = {'A':3,'B':1,'C':0,'D':1}

output = analyse(votesDic,seatsDic)

