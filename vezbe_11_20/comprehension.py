# Generisati listu 0-n
# u novu listu ubaciti sve brojeve koji su
# kvadrati nekog broja
from math import sqrt

def generate_new_list(n):
    return [x for x in range(1, n+1)]

def get_sqrts(l):
    return [x for x in l if sqrt(x).is_integer()]

def main():
    n = 50
    l = generate_new_list(n)
    sqrts = get_sqrts(l)
    print(sqrts)
if __name__ == "__main__":
    main()