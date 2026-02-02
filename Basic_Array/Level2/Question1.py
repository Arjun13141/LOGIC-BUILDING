## Input an element x — check if it exists in the array.

def check_element(arr, x):
    if x in arr:
        return "Element found"
    else:
        return "Element not found"
    
x = int(input("Enter the Element to search : "))
arr = [1,2,3,4,5]

print(check_element(arr,x))