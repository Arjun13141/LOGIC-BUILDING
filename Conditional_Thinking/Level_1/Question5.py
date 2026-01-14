## 5. Check if a given year is a leap year.
num = 2024
if (num%400==0) or (num%100!=0 and num%4==0):
    print("yes")
else:
    print("No")