def createNetwork():
    myFile = open('network.txt', 'r')
    network={}
    for line in myFile:
        lineAsList = line.split()
        fromStation = lineAsList[0]
        network = addStationIfNotPresent(network,fromStation)
        lineAsList.pop(0)
        for toStation in lineAsList:
            network=makeConnection(network,fromStation, toStation)
            network=makeConnection(network,toStation, fromStation)
    return network

def addStationIfNotPresent(network, name):
    if name not in network:
        network[name] = set()
    return network

def makeConnection(network, fromStation, toStation):
	network = addStationIfNotPresent(network, fromStation)
	network[fromStation].add(toStation)
	return network
    

network = createNetwork()
print("The network created is ", network)
