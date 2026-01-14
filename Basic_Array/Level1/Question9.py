## 9. Find the index of the minimum element.

arr = [10,20,3,4,5,9,7]
mini_ele = arr[0]
ind = 0

for i in range(len(arr)):
    if arr[i]<mini_ele:
        mini_ele = arr[i]
        ind = i
print("The minimum element index is ", ind)