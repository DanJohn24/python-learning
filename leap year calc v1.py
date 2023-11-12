year = int(input("Please enter a year: "))

if (year % 4 == 0 and not year % 100 == 0):
    print ("The year ",year," is a leap year")
elif (year % 400 == 0):
    print ("The year ",year," is a leap year")
elif (year % 100 == 0):
    print ("The year ",year," is not a leap year")
else:
    print("The year ",year," is not a leap year")
