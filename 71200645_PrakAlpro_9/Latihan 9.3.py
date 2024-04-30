def split_kata():
    with open ("Berita.txt", "r") as file:
        kata = []
        hasil = file.read()
        pisah = hasil.split()
        for i in pisah:
            if i not in kata:
                kata.append(i)
        print(kata)
    file.close()
    
split_kata()