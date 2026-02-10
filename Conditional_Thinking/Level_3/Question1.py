## Take a 3-digit number and check if all digits are distinct.
def is_distinct(num):
    if num>=100 and num<=999:
        digit = str(num)
        if len(set(digit))==3:
            print("yes")
        else:
            print("No")
    else:
        print("not a 3 digit number")

num = 121
is_distinct(num)