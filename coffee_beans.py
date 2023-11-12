import random

def output():
    print ("There are now ",blackAm," black beans, and ",whiteAm," white beans")

availible_options = []


blackAm = int(input("How many black beans to start: "))
whiteAm = int(input("How many white beans to start: "))

print("\n")
while (blackAm and whiteAm) > 1:
    if (blackAm >= 2):
        availible_options.append(1)
    if (whiteAm >= 2):
        availible_options.append(2)
    if (whiteAm >= 1 and blackAm >= 1): 
        availible_options.append(3)

    choice = random.choice(availible_options)

    if choice == 1:
        print("black - 2 and white + 1")
        print("\n")
        blackAm -= 2
        blackAm += 1
    if choice == 2:
        print("white - 2 and black + 1")
        print("\n")
        whiteAm -= 2
        whiteAm += 1
    if choice == 3:
        print("black - 1")
        print("\n")
        blackAm -= 1


print("\n")
output()
print ("is the final result")
