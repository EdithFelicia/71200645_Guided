try:   
    user = int(input("Masukkan bulan (1-12): "))
    if 1 <= user <= 12:
        if user == 2:
            print("Jumlah hari: 29")
        elif user in [4, 6, 9, 11]:
            print("Jumlah hari: 30")
        else:
            print("Jumlah hari: 31")
    else:
        print("Bulan yang diinputkan tidak valid")
except:
    print("Anda salah memasukkan bulan")