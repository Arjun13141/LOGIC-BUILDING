## 7. Count how many elements are even and odd.
even = 0
odd = 0

arr  = [1,2,3,4,5,6]

for num in arr:
    if num%2==0:
        even = even +1
    else:
        odd = odd + 1

print(odd , even)