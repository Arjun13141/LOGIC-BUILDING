## Check if a number is even or odd.
def even_odd(num):
    if num%2==0:
        return f"{num} is a EVEN number."
    else:
        return f"{num} is a ODD number."
    
print(even_odd(0))