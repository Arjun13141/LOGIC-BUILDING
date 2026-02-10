## Check if a number is a multiple of 7 or ends with 7.
def check_number(num):
    if num %7 == 0:
        return "yes, number is multiple"
    elif num%10 == 7:
        return "yes, number end with 7"
    else:
        return "nither number is multiple of 7 nor end with 7"
    
num = int(input("Enter an integer: "))
print(check_number(num))
