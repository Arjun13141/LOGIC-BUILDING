### 8. Find the index of the maximum element.

arr = [1,2,3,4,5,9,7]
max_ele = arr[0]
ind = 0

for i in range(len(arr)):
    if arr[i]>max_ele:
        max_ele = arr[i]
        ind = i

print("The index of the largest number is ", ind)