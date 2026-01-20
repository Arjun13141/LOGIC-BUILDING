## Take two numbers and determine whether both are even, both are odd, or one is even and one is odd

def check_2_even_odd(num1, num2):
    if num1%2==0 and num2%2==0:
        print("both are even")
    elif num1%2!=0 and num2%2!=0:
        print("Both are odd")
    else: 
        print("One is even and one is odd")

check_2_even_odd(2,5)