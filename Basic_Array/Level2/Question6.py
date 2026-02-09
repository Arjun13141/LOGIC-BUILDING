## Find the sum of even elements only.
def even_sum(arr):
    sum = 0
    for num in arr:
        if num%2==0:
            sum += num
    return sum

arr = [10, 21, 32, 43, 54, 65]
print(even_sum(arr))