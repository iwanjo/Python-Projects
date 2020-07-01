# Given an integer, , perform the following conditional actions:

# If  is odd, print Weird
# If  is even and in the inclusive range of 2  to 5, print Not Weird
# If  is even and in the inclusive range of  to 6, 20 print Weird


def weirdOrNot(n):
    
    if(n % 2 != 0):
        return "Weird"

    elif (n % 2 == 0) and range(2, 5):
        return "Not Weird"

    elif (n % 2 ==0) and range(6, 20):
        return "Weird"

    elif (n > 20):
        return "Weird"

print(weirdOrNot(3))