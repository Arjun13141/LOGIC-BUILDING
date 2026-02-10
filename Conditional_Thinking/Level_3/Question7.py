## Check if an amount can be evenly divided into 2000, 500, and 100 currency notes
def check_divisible(amnt):
    if amnt%100==0:
        return "Yes"
    else:
        return "No"
    
amount = int(input("Enter the amount: "))
print(check_divisible(amount))