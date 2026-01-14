## input n and take n integers into an array; print them.

n = int(input("Enter how many number you want: "))

arr = []
for i in range(n):
    num = int(input(f"Enter number {i+1}: "))
    arr.append(num)

print("The number are ", arr)