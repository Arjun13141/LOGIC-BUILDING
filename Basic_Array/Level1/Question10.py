## 10. Take n elements and print only those greater than a given value k.

n = int(input("Enter the length of array: "))
arr = []

for i in range(n):
    num = int(input(f"Enter the value for {i+1}"))
    arr.append(num)

k = int(input("Give the threshold value."))

for num in arr:
    if num>k:
        print(num)