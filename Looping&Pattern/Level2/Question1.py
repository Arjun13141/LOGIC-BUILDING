## 1. Count the number of digits in a given number
def count_digit_math(num):
    num = abs(num)

    if num == 0:
        return 1
    count = 0
    while num>0:
        num//=10
        count+=1
    return count

print(count_digit_math(123))