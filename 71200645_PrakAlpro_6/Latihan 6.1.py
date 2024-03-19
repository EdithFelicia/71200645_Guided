def prima_terdekat():
    angka = int(input("Masukkan bilangan: "))
    if angka <= 2:
        return None  # Tidak ada bilangan prima yang lebih kecil dari 2
    
    for i in range(angka - 1, 1, -1):
        prima = True
        for j in range(2, int(i ** 0.5) + 1):
            if i % j == 0:
                prima = False
                break
        if prima:
            print(f"Bilangan prima terdekat < {angka} adalah {i}")
            return i

prima_terdekat()