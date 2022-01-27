
import math as np
# import display_results as dr
import multiprocessing as mp
import time
import tracemalloc
import sys

# Metoda generise koordinate svih polja na tabli
def generate_coordinates(n, m):
    for i in range(n):
        for j in range(m):
            yield (i,j)

# Metoda racuna razdaljinu izmedju dva polja
def calculate_distance(field, special_field):
    return np.sqrt((field[0] - special_field[0]) ** 2 + (field[1] - special_field[1]) ** 2)

# Metoda racuna razdaljinu obicnog polja do svih specijalnih polja
def calculate_distances(field, special_fields):
    for i in range(len(special_fields)):
        distance = calculate_distance(field, special_fields[i])
        yield distance, i

def prepare_arguments(table_fields, special_fields):
    for table_field in table_fields:
        yield table_field, special_fields

def _worker(args):
    table_field, special_fields = args
    return min(calculate_distances(table_field, special_fields))[1]

def multiprocessing(n, m, special_fields):
    table_fields = generate_coordinates(n,m)
    with mp.Pool(8) as pool:
        res = pool.imap(
            _worker,
            prepare_arguments(table_fields, special_fields),
            chunksize=n
        )
        return [r for r in res]

if __name__ == "__main__":
    n = 10
    m = 10
    # points = ["1,3", "3,2", "6,8", "9,6", "5,5", "123,555", "345,543"]
    # special_fields = dr.read_points(points)
    special_fields = [(1,3), (3,2), (6,8), (9,6), (5,5)]

    print("Multiprocessing:")

    # tracemalloc.start()
    start = time.time()
    result = multiprocessing(n, m, special_fields)
    end = time.time()
    # current, peak = tracemalloc.get_traced_memory()
    # print(f"Current memory usage is {current / 10**6}MB; Peak was {peak / 10**6}MB")
    # tracemalloc.stop()
    print("Execution time:", end - start)
    print(result)
    # dr.display_results(result, n, m, points)
    # dr.show_table(result, n, m, points)