#Python program to find the largest element in an array

def largest_elem(arr, n):

    #We initialise the max element
    max_elem = arr[0]

    #traverse the array elements and compare with current max
    for i in range(1, n):
        if arr[i] > max_elem:
            max_elem = arr[i]

    return max_elem


arr = [21, 10, 29, 34, 13, 5, 3, 2]
n = len(arr)
largest_element = largest_elem(arr, n)
print("The largest element in the array is: ", largest_element)