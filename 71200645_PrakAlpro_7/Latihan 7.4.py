def panjang_pendek_kata():
    kalimat = input("Masukkan kalimat: ")
    kata = kalimat.split()
    
    terpendek = kata[0]
    terpanjang = kata[0]

    for i in kata:
        if len(i) < len(terpendek):
            terpendek = i
        if len(i) > len(terpanjang):
            terpanjang = i
    print(f"terpendek: {terpendek}, terpanjang: {terpanjang}")
    
panjang_pendek_kata()