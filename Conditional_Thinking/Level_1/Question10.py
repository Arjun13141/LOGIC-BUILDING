## Take a character and check whether it’s uppercase, lowercase, a digit, or a special character
char = "%"
if char.isupper():
    print("Upppercase")
elif char.islower():
    print("Lowercase")
elif char.isdigit():
    print("Digit")
else:
    print("Special character")