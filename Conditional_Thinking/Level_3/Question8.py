## Check if a number lies within the range [100, 999].
def check_range(num):
    if num>=100 and num<=999:
        return "yes, it lies btw the range"
    else:
        return "Number does NOT lie within the range"
    
num = int(input("Enter the number: "))
print(check_range(num))