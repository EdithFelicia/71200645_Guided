def konversi(data, target):
    print("Data:", data)
    hasil = None

    if target == "set":
        hasil = set(data)
        print("Konversi ke Set:", hasil)
    elif target == "list":
        if isinstance(data, set):
            hasil = list(data)
        else:
            hasil = list(data)
        print("Konversi ke List:", hasil)
    elif target == "tuple":
        if isinstance(data, set):
            hasil = tuple(data)
        else:
            hasil = tuple(data)
        print("Konversi ke Tuple:", hasil)

    return hasil

list_data = ["Hello", 2, 23.4, 2, 1]
tuple_data = (4, 5, "Langkah", 5, 4)

list_to_set = konversi(list_data, "set")
set_to_list = konversi(list_to_set, "list")
tuple_to_set = konversi(tuple_data, "set")
set_to_tuple = konversi(tuple_to_set, "tuple")