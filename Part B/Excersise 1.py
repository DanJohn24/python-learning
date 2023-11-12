def getCons(filename):   
    file = open(filename)
    conSet = set()

    for line in file:
        readLines = file.readline()
        split = readLines.split(":")

        if split[0] == "_Constituency":
            conSet.add(split[1])

    file.close()  
    print(conSet)

file = "ukeu2019.txt"

getCons(file)
