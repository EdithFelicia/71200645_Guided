def hitung_string():
    kalimat = input("Masukkan kata: ").lower()
    kata = input("Jumlah kemunculan kata yang diinginkan: ")
    if kata in kalimat:
        hitung = kalimat.count(kata)
        print(f"{kata} ada {hitung} buah")

hitung_string()