## 4. Check if one of two given numbers is a multiple of the other.
def check_multiple(x,y):
    if y!=0 and x%y==0:
        print(f"{x} is a multiple of {y}.")
    elif x!=0 and y%x==0:
        print(f"{y} is a multiple of {x}.")
    else:
        print("Nither of them are multiple of each other.")

check_multiple(21,7)