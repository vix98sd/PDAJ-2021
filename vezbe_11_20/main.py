def main():
    l = [1,2,3,4,5,6, 10, 10, 6, 6]
    new_list = []

    # Ova for petlja ima istu funkcionalnost kao i 
    # linija za kreiranje promenljive new_list_2
    for num in l:
        if num % 2 == 0 and num != 10:
            new_list.append(num)
    
    print(new_list)

    new_list_2 = [num for num in l if num % 2 == 0 and num != 10]
    print(new_list_2)

    # Moguce je dodati i izracunat element
    new_list_2 = [(num, num**2) for num in l if num % 2 == 0 and num != 10]
    print(new_list_2)

    # Postoji takodje i dictionary comprehension
    d = {"a":2,"b":3,"c":5,"d":2}
    new_dict = {k:v for (k, v) in d.items() if v % 2 == 0}
    print(new_dict)

if __name__ == "__main__":
    main()