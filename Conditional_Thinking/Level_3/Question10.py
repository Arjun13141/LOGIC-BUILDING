## Check whether a number is a perfect square (without using the square root function)
def is_perfect_sq(num):
    if num<0:
        return "negetive number"
    
    i = 0
    while i*i <= num:
        if i*i == num:
            return True
        i+= 1
    return False

num = int(input("Enter a number: "))
print("Perfect square ✅" if is_perfect_sq(num) else "Not a perfect square ❌")
