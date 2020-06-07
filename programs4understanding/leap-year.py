#In this program we will be able to check if a given year is a leap year or not

#Let us get user input as an integer from the user

year = int(input("Enter a year: "))

if (year % 4) == 0:
    print("{0} is a leap year".format(year))

else:
    print("{0} is not a leap year".format(year))