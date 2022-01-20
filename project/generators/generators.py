
import numpy as np
import display_results as dr
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
    for special_field in special_fields:
        distance = calculate_distance(field, special_field)
        yield distance

# Metoda racuna distance 
def find_all_distances(table_fields, special_fields):
    for field in table_fields:
        distances = calculate_distances(field, special_fields)
        yield distances

# Metoda trazi indeks najblizeg specijanog polja
def find_nearest_index(distances):
    nearest = sys.maxsize
    index = -1
    i = 0
    for distance in distances:
        if distance < nearest:
            nearest = distance
            index = i
        i = i + 1
    return index

# Metoda trazi najbliza specijalna polja za sva polja na tabli
def find_all_nearest_fields(all_distances):
    result = []
    for distances in all_distances:
        nearest = find_nearest_index(distances)
        result.append(nearest)
    return result

def generators(n, m, special_fields):
    table_fields = generate_coordinates(n,m)
    all_distances = find_all_distances(table_fields, special_fields)
    result = find_all_nearest_fields(all_distances)
    return result

if __name__ == "__main__":
    n = 10
    m = 10
    special_fields = [(1,3), (3,2), (6,8), (9,6), (5,5)]
    points = ["1,3", "3,2", "6,8", "9,6", "5,5"]
    result = generators(n, m, special_fields)

    dr.display_results(result, n, m, points)
    # dr.show_table(result, n, m, points)