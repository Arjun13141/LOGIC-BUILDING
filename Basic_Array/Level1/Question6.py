## Count how many elements are positive, negative, or zero.

positive = 0
negative = 0
zero = 0

arr = [-1, -2, 0, 1, 2]

for num in arr:
    if num>0:
        positive += 1
    elif num<0:
        negative += 1
    elif num == 0:
        zero += 1 

print(positive)
print(negative)
print(zero)