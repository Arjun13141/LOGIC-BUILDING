## Count how many numbers are divisible by 3 and 5 both.
def divideBy3_5(arr):
    count = 0
    for num in arr:
        if num%3==0 and num%5==0:
            count+=1
    return count

arr = [10, 15, 30, 45, 50, 60, 75, 90]
print(divideBy3_5(arr))