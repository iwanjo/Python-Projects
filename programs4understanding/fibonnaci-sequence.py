#Program to display the fibonacci sequence to the nth term

numberTerms = int(input("How Many terms?: "))

n1, n2 = 0, 1
count = 0

if numberTerms <= 0:
    print("Please enter a positive integer")

elif numberTerms == 1:
    print("Fibonnaci Sequence upto", numberTerms, ":")
    print(n1)

else:
    print("Fibonnaci Sequence: ")
    while count < numberTerms:
        print(n1)
        nth = n1+ n2

        n1 = n2
        n2 = nth
        count = count + 1