## Find the maximum element in an array.

arr = [1,2,3,4,5]
max_el= arr[0]

for i in arr:
    if i>max_el:
        max_el = i

print("The maximum elment is ", max_el)