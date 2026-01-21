## 3. Check if a number is a palindrome.
def is_palindrome(num):

    if num<0:
        return False
    original = num
    rev = 0
    while num>0:
        reminder = num%10
        rev = rev*10 + reminder
        num = num//10
    return original == rev
    
print(is_palindrome(121))