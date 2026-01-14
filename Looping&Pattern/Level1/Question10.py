## Print the product of digits of a given number.

n = 123
product = 1

while n>0:
    digit = n%10
    product = product * digit
    n = n//10

print(product)