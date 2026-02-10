## Take a 4-digit number and check if the first and last digits are equal.
def check_first_last_equal(num):
    if num<1000 and num>9999:
        return "not a 4 digit value"
    a = num//1000
    b = num%10
    if a==b:
        return "first and last digit are equal"
    else:
        return "first and last digit are not equal"
    
num = int(input("Enter a 4-digit number: "))
print(check_first_last_equal(num))
