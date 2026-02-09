## Find the count of prime numbers in the array
def is_prime(n):
    if n<=1:
        return False
    for i in range(2,int(n**0.5)+1):
        if n%i==0:
            return False
    return True

def count_primes(arr):
    count= 0
    for num in arr:
        if is_prime(num):
            count+=1
    return count

arr = [10, 21, 32, 43, 54, 65, 7, 11]
print("Count of prime numbers:", count_primes(arr))
