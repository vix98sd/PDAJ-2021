# Biblioteka za pracenje iskoriscenja resursa
# Meri koriscene resurse od pozivanja
# .start() do pozivanja .stop()
import tracemalloc
from math import sqrt

def generate_new_list(n):
    return [x for x in range(1, n+1)]

def get_sqrts(l):
    return [x for x in l if sqrt(x).is_integer()]

def main():
    tracemalloc.start()
    n = 10000
    sqrts = get_sqrts(generate_new_list(n))
    current, peak = tracemalloc.get_traced_memory()
    print(f"Current memory usage is {current / 10**6}MB; Peak was {peak / 10**6}MB")
    tracemalloc.stop()

if __name__ == "__main__":
    main()