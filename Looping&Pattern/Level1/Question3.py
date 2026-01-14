## Print all odd numbers between 1 and 100.
for i in range(1,100):
    if i%2!=0:
        print(i)

## better approch
for i in range(1,100,2):
    print(i)