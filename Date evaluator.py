def isLeapYear(year):
    if (year%4==0 and year%100!=0) or year%400==0:
        return True
    else:
        return False

def daysIn(year, month):
    if month in [1,3,5,7,8,10,12]:
        return 31
    elif month in [4,6,9,11]:
        return 30
    elif (isLeapYear(year)) and month == 2:
        return 29
    else:
        return 28

def validGreg(year, month, day):
    if (year >= 1753 and 1<= month <=12 and 1<= day <= daysIn(year, month)):
        return True
    else:
        return False

year = int(input("Enter a year: "))
month = int(input("Enter a month: "))
day = int(input("Enter a day: "))

written_months = ["January", "February", "March", "April", "May", "June", "July", "August","September","November","December"]

if validGreg(year, month, day):
    print("Valid gregorian date")
    
    if isLeapYear(year):
        print("The",year, "is a leap year")
    else:
        print("The",year, "is not a leap year")

    print("In the year ",year, ",in the month of",written_months[month-1],"(",month,")" "there are:", daysIn(year, month), "days")
else:
    print("Not valid gregorian date, no data will be displayed")
