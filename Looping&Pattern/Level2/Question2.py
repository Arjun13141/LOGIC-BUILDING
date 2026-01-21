## 2. Print the reverse of a given number.
## with this method we can check palindrome as well
def rev_num(num):
    num = abs(num)

    if num==0:
        return 1
    
    rev = 0
    while num>0:
        reminder = num%10
        rev = rev*10 + reminder
        num = num//10
    return rev

print(rev_num(123))