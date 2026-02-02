## Find the first occurrence of a given number.

def first_occurrence(arr, x):
    for i in range(len(arr)):
        if arr[i]==x:
            return f"The index of that element {x} is {i}" 
    return "Sorry, element not found"

arr = [10,20,30,40,50]
x = 20
print(first_occurrence(arr, x))