## 8. Take an alphabet character and check if it lies between ‘a’ and ‘m’ or ‘n’ and ‘z’.
def check_alphabet_range(ch):
    ch = ch.lower()
    
    if 'a' <= ch <= 'm':
        return f"{ch} lies between 'a' and 'm'"
    elif 'n' <= ch <= 'z':
        return f"{ch} lies between 'n' and 'z'"
    else:
        return "Invalid input! Please enter an alphabet character."

c = "c"

print(check_alphabet_range(c))
