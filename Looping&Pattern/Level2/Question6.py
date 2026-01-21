## 6. Check if a number is a perfect number.
def is_perfect_num(num):
    if num<=0:
        return False
    
    divs= 0
    for i in range(1, num):
        if num%i==0:
            divs = divs+i
    return divs==num

print(is_perfect_num(6))