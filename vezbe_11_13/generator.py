def number_generator(n):
    for i in range(1,n+1):
        print(i)

if __name__ == "__main__":
    n = input("Insert number n:")
    n = int(n)
    number_generator(n)