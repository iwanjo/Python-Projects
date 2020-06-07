#This python program will check if a given number is odd or even

#a number is even if it is perfectly divisible by 2

num = int(input("Enter a number: "))

if (num % 2 == 0):
    print("{0} is even".format(num))

else:
    print("{0} is odd".format(num))