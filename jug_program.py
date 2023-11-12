def output():
    print("jug A now has ",volA,"L, jug B has ",volB,"L")
    print("You are now on your ",iNumber," iteration")

capA = int(input("Please enter total capacity of jug 1 (L): "))
capB = int(input("Please enter starting volume of jug 2 (L): "))

iNumber = 0 #iteration counter

volA = 0
volB = 0

desired_volume = int(input("Please enter desired volume (L): "))

while (volA != desired_volume):
    iNumber += 1
    if (volA == 0):
        volA = capA
        output()
    elif (volB == capB):
        volB = 0
        output()
    else:
        #if the volume of jugA is smaller than the empty space of jugB volA will be added to jugB - and will be subtracted from jug A
        #otherwise jug B will be effectivelly filled - and the fillage volume subtracted from jugA
        transfer = min(volA, capB - volB)
        volB = volB + transfer
        volA = volA - transfer
        output()
print("program is done")
