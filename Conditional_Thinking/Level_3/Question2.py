## Take a 3-digit number and determine if the middle digit is the largest, smallest, or neither.
def what_is_mid(num):
    if num<100 and num<999:
        return "Number is less then three digit"
    a = num//100
    b = (num//10)%10
    c = num%10
    if b>a and b>c:
        return f"{b} is largest number in {num}"
    elif b<a and b<c:
        return f"{b} is the smallest middle number in {num}"
    else:
        return "Middle digit is neither largest nor smallest"
    

num = int(input("Enter a 3-digit number: "))
print(what_is_mid(num))

