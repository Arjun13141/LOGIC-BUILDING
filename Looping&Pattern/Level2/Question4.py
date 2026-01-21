## 4. Find the sum of digits of a number.
def num_sum(num):
    num = abs(num)

    total = 0
    while num>0:
        reminder = num%10
        total += reminder
        num = num//10
    return total

print(num_sum(123))