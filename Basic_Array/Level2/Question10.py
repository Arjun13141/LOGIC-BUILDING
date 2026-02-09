## Count how many elements are perfect squares
import math
def count_perfect_sq(arr):
    count= 0
    for num in arr:
        root = int(math.sqrt(num))
        if root*root == num:
            count+= 1
    return count

arr = [4, 7, 9, 16, 20, 25, 30]
print("Count of perfect squares:", count_perfect_sq(arr))
