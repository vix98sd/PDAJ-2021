
import math as np
# import display_results as dr
import time
import tracemalloc

# Metoda generise koordinate svih polja na tabli
def generate_coordinates(n, m):
    coordinates = []
    for i in range(n):
        for j in range(m):
            coordinates.append((i,j))
    return coordinates

# Metoda racuna razdaljinu izmedju dva polja
def calculate_distance(field, special_field):
    return np.sqrt((field[0] - special_field[0]) ** 2 + (field[1] - special_field[1]) ** 2)

# Metoda racuna razdaljinu obicnog polja do svih specijalnih polja
def calculate_distances(field, special_fields):
    distances = []
    for special_field in special_fields:
        distance = calculate_distance(field, special_field)
        distances.append(distance)
    return distances

# Metoda trazi indeks najblizeg specijanog polja
def find_nearest_index(distances):
    nearest = min(distances)
    for i in range(len(distances)):
        if distances[i] == nearest:
            return i

# Metoda trazi najbliza specijalna polja za sva polja na tabli
def find_all_nearest_fields(all_distances):
    result = []
    for distances in all_distances:
        nearest = find_nearest_index(distances)
        result.append(nearest)
    return result

def sequential(n, m, special_fields):
    table_fields = generate_coordinates(n,m)
    all_distances = []
    for field in table_fields:
        distances = calculate_distances(field, special_fields)
        all_distances.append(distances)
    result = find_all_nearest_fields(all_distances)
    return result

if __name__ == "__main__":
    n = 10
    m = 10
    # points = ["1,3", "3,2", "6,8", "9,6", "5,5", "123,555", "345,543"]
    # special_fields = dr.read_points(points)
    special_fields = [(1,3), (3,2), (6,8), (9,6), (5,5)]

    print("Sequential:")

    # tracemalloc.start()
    start = time.time()
    result = sequential(n, m, special_fields)
    end = time.time()
    # current, peak = tracemalloc.get_traced_memory()
    # print(f"Current memory usage is {current / 10**6}MB; Peak was {peak / 10**6}MB")
    # tracemalloc.stop()
    print("Execution time:", end - start)
    print(result)

    # dr.display_results(result, n, m, points)
    # dr.show_table(result, n, m, points)