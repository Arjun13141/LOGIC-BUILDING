## 10. Print sum of first n terms of Fibonacci series.
def sum_fibonacci(num):
    a,b = 0, 1
    sum = 0
    for _ in range(num):
        sum += a
        a,b = b, a+b
    return sum

print(sum_fibonacci(5))