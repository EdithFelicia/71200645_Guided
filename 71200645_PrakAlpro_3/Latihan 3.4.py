try:
    angka_1 = int(input("Masukkan sisi 1: "))
    angka_2 = int(input("Masukkan sisi 2: "))
    angka_3 = int(input("Masukkan sisi 3: "))

    if angka_1 == angka_2 == angka_3:
        print("3 sisi sama")
    elif angka_1 == angka_2 or angka_1 == angka_3 or angka_2 == angka_3:
        print("2 sisi sama")
    elif angka_1 != angka_2 != angka_3:
        print("Tidak ada yang sama")
except:
    print("Anda harus memasukkan bilangan bulat")