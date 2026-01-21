## 5. Check if a number is an Armstrong number.
def is_armstrong(num):

    num_str = str(abs(num))
    power = len(num_str)

    total = sum(int(digit)**power for digit in num_str)

    return total == abs(num)

print(is_armstrong(153))