## 9. Print Fibonacci series up to n terms.
def fibonacci(num):
    f0 = 0
    f1 = 1
    series = []
    for _ in range(0, num+1):
        series.append(f0)
        f0, f1 = f1, f0+f1
    return series

print(fibonacci(5))