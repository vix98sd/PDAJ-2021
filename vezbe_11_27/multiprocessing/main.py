import multiprocessing as mp
import tracemalloc

def square_function(num):
    ret = []
    for i in range(num):
        ret.append(i**2)
    return ret

def square_by_two(num):
    li = square_function(num)
    ret = []
    for l in li:
        ret.append(l/2)
    return ret

def main():
    tracemalloc.start()
    with mp.Pool() as pool:    # pool je nacin na koji cemo rasporedjivati taskove
        res = pool.imap_unordered(square_by_two, range(30))
        for r in res:
            print(r)
        # square_by_two(100000)

    current, peak = tracemalloc.get_traced_memory()
    print(f"Current memory usage is {current / 10**6}MB; Peak was {peak / 10**6}MB")
    tracemalloc.stop()

if __name__ == "__main__":
    main()