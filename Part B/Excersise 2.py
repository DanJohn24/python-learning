def getAllParties(fileName):
    file = open(fileName)
    compList = []

    for eachLine in file:
        readLines = file.readline()
        split = readLines.split(":")
        compList.append(split)
        
    return compList
    file.close()
     

print(getAllParties('ukeu2019.txt'))
