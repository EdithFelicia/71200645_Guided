menu = [
    ("Nasi goreng ayam", 19_000),
    ("Nasi goreng ayam + telor", 23_000),
    ("Nasi goreng kambing", 35_000),
    ("Nasi goreng kambing + telor", 39_000),
    ("Nasi goreng seafood", 24_000),
    ("Nasi goreng seafood + telor", 28_000),
    ("Nasi goreng ati", 21_000),
    ("Nasi goreng ati + telor", 25_000),
    ("Teh es/anget", 5_000),
    ("Jeruk", 8_000),
]
pesanan = []


def tampil():
    print("Selamat datang di py cafe")
    print("Berikut adalah menu yang tersedia:")
    print("----------------------------------------------\n")
    for item in range(len(menu)):
        print(f"{item+1}.\t{menu[item][1]}\t{menu[item][0]}")
        if item == len(menu):
            print("\n Bayar semua pesanan?")
    pilihan = input(
        "\nApa pesanan anda (ketik 'bayar' untuk mengakhiri pesanan dan membayar): "
    )
    if pilihan == "1":
        pesanan.append(menu[0])
        tampil()
    elif pilihan == "2":
        pesanan.append(menu[1])
        tampil()
    elif pilihan == "3":
        pesanan.append(menu[2])
        tampil()
    elif pilihan == "4":
        pesanan.append(menu[3])
        tampil()
    elif pilihan == "5":
        pesanan.append(menu[4])
        tampil()
    elif pilihan == "6":
        pesanan.append(menu[5])
        tampil()
    elif pilihan == "7":
        pesanan.append(menu[6])
        tampil()
    elif pilihan == "8":
        pesanan.append(menu[7])
        tampil()
    elif pilihan == "9":
        pesanan.append(menu[8])
        tampil()
    elif pilihan == "10":
        pesanan.append(menu[9])
        tampil()
    elif pilihan.lower() == "bayar":
        print("\n\nBerikut adalah pesanan anda: ")
        print("----------------------------------------------")
        for item in range(len(pesanan)):
            print(f"{item+1}.\t{pesanan[item][1]}\t{pesanan[item][0]}")
        print("\nStruk akan dicetak")
        cetak()
    else:
        tampil()


def cetak():
    pesan = open("Modul/pt9_alpro.txt", "w")
    pesan.write("----------------------------------------------\n")
    pesan.write("                  PY CAFE                     \n")
    pesan.write("----------------------------------------------\n")
    for item in range(len(pesanan)):
        pesan.write(f"{item+1}.\t{pesanan[item][1]}\t{pesanan[item][0]}\n")
    # pesanan[item][1] => Untuk mengambil harga
    # pesanan[item][0] => Untuk mengambil nama makanan
            

tampil()
