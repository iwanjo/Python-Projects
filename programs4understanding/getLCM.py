#In this program we will find the LCM of two numbers

def get_lcm(a, b):

    if a > b:
        greater = a

    else:
        greater = b

    while True:
        if((greater % a == 0) and (greater % b ==0 )):
            lcm = greater
            break

        greater += 1

    return lcm

num1 = 4
num2 = 6

print("The LCM is ", get_lcm(num1, num2))