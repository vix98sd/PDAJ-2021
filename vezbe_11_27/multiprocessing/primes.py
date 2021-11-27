# napisati program koji trazi proste brojeve
# od 2 do N (N=1000, N=10000, N=100000, N=1000000)
# sekvencijalno i preko map, imap, i imap_unordered,
# koristiti tracemalloc i uporediti rezultate

import multiprocessing as mp
import tracemalloc
from math import sqrt

def all_primes(max):
    ret = []
    for i in range(3, max+1):
        if is_prime(i):
            ret.append(i)
    return ret

def is_prime(n):
    for i in range(2, int(sqrt(n))+1):
        if n % i == 0:
            return False
    return True

def main():
    tracemalloc.start()
    pool = mp.Pool()
    primes = pool.imap(all_primes, range(3, 1000), chunksize=250)
    for p in primes:
        pass
    pool.terminate()
    
    current, peak = tracemalloc.get_traced_memory()
    print(f"Current memory usage is {current / 10**6}MB; Peak was {peak / 10**6}MB")
    tracemalloc.stop()
    
if __name__ == "__main__":
    main()