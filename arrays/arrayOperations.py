#demonstrate various array operations in python

import array

#We can initialise an array with signed integer - i

myArray = array.array('i', [2, 4, 6, 8])


#Print the original array to the console
print("The array is: ", end=" ")
for i in range(0,4):
    print(myArray[i], end=" ")

print("\r")

#we can use the append() procedure to insert a new value to the array

myArray.append(10)

print("The new array is: ", end=" ")
for i in range(0, 5):
    print(myArray[i], end= " ")


#We can use insert to insert a value at a specific position in the array

myArray.insert(0, -2)

print("\nThe new array after inserting at a given position is: ", end=" ")
for i in range(0, 6):
    print(myArray[i], end=" ")


myNewArray = array.array('i', [1, 2, 5, 7, 9])

print("\r\n")
print("My new array is: ", end=" ")
for j in range(0, 5):
    print(myNewArray[j], end=" ")


#using remove
myNewArray.remove(2)

print("\r")
print("After removing the element with 2 my new array is: ", end=" ")
for i in range(0, 4):
    print(myNewArray[i], end=" ")


#using pop()

print("\nThe popped element is: ", end="")
print(myNewArray.pop(0))
