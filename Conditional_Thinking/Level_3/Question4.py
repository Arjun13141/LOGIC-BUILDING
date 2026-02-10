## Check whether a given integer is single-digit, double-digit, or multi-digit.
def check_digit(num):
    n = abs(num)

    if n<10:
        return "single digit number"
    elif n<100:
        return "Double digit number"
    else:
        return "multi-digit"
    
num = int(input("Enter an integer: "))
print(check_digit(num))
