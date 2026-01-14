## Print the sum of all even numbers up to n.
n = 5
even_sum = 0
for i in range(n+1):
    if i%2==0:
        even_sum = even_sum + i

print(even_sum)