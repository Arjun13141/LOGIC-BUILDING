## Print the sum of all odd numbers up to n.

n = 5
odd_sum = 0

for i in range(n+1):
    if i%2!=0:
        odd_sum += i 

print(odd_sum)