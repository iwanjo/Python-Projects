#In this program we will find the factorial of a number provided by the user

num = int(input("Enter a number: "))

factorial = 1

if num < 0:
    print("There is no factorial for negative numbers")

elif num == 0:
    print("Factorial of 0 is 1")

else:
    for i in range(1, num + 1):
        factorial = factorial * i

    print("The factorial of ", (num), "is ", factorial)