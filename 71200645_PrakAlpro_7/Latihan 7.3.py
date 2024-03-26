def hapus_spasi():
    kalimat = input("Masukkan kalimat: ")
    hasil = kalimat.split()
    gabung = " ".join(hasil)
    print(gabung)
    

hapus_spasi()