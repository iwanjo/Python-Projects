#program for a simple calc

def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    return a / b

print("----Calculator Main Menu----")

print("1. Add")
print("2. Subtract")
print("3. Multiply")
print("4. Divide")


#user input

while True:

    userChoice = input("Enter Your Choice: ")

    if userChoice in ('1', '2', '3', '4'):
        num1 = float(input("Enter the first number: "))
        num2 = float(input("Enter the second number: "))

        if userChoice == '1':
            print(num1, " + ", num2, " = ", add(num1, num2))

        elif userChoice == '2':
            print(num1, " - ", num2, " = ", subtract(num1, num2))

        elif userChoice == '3':
            print(num1, " * ", num2, " = ", multiply(num1, num2))

        elif userChoice == '4':
            print(num1, " / ", num2, " = ", divide(num1, num2))

        break

    else:
        print("Invalid Input")