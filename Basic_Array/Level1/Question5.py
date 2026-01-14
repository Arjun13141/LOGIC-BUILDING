## Find the minimum element in an array.

arr = [1,2,3,4,5]
min_el = arr[0]

for num in arr:
    if min_el>num:
        min_el = num

print("The minimum element is ", min_el)