from math import sqrt

def find_max(ar):
    return max(ar)

def all_primes(max):
    for i in range(3, max+1):
        if is_prime(i):
            print(i)

def is_prime(n):
    for i in range(2, int(sqrt(n))+1):
        if n % i == 0:
            return False
    return True

if __name__ == "__main__":
    ar = [1,6,2,5,11,18,14,9]
    max = find_max(ar)
    all_primes(max)