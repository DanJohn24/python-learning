file = "ukeu2019.txt"

#Excersise 6 (1)
def getCons(fileName):   
    file = open(fileName)
    conSet = []
    #
    for line in file:
        strip = line.strip()
        split = strip.split(":")
        #
        if split[0] == "_Constituency":
            conSet.append(split[1])
    #
    file.close()  
    return conSet

'''
print(getCons(file))
'''

#Excersise 7 (2)
def getParties(fileName):
    file = open(fileName)
    partyList = []
    #
    for line in file:
        strip = line.strip()
        split = strip.split(":")

        if len(split) >= 2 and split[0] != "_Constituency" and split[0] != "_Seats":
            partyList.append(split[0])
    #
    file.close()
    return(partyList)

'''
print(getParties(file))
'''

#Excersise 8 (3)
def getVotesForConstituency (fileName,con):
    file = open(fileName)
    partiesDict = {}
    i = 0
    valid = False
    #
    for line in file:
        strip = line.strip()
        split = strip.split(":")
        #
        if len(split) >= 2 and split[1] == con:  
            valid = True
        elif len(split) >= 2 and valid == True and split[0] != "_Seats":
            partiesDict[split[0]] = split[1] 
        elif valid == True and len(split) < 2:
            break #sorry
    #
    file.close()
    return partiesDict

'''
print(getVotesForConstituency(file, "West Midlands"))
'''

#excersise 9 (4)
def getTotalVotes (fileName):
    file = open(fileName)
    votesDict = {}
    #
    for line in file:
        strip = line.strip()
        split = strip.split(":")
        #
        if split[0] != "_Constituency" and split[0] != "_Seats":
            if len(split) >= 2 and split[0] in votesDict: #handle duplicates
                votesDict[split[0]] = int(votesDict[split[0]]) + int(split[1])
            elif len(split) >= 2: #handle new instances
                votesDict[split[0]] = split[1]
    #
    file.close()
    return votesDict

'''
print(getTotalVotes(file))
'''

