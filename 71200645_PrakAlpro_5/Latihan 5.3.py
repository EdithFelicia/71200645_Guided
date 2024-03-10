def penghitung_IPS():
    jumlah = int(input("Berapa jumlah mata kuliah? "))
    total_sks = jumlah * 3
    total_nilai = 0
    
    for i in range(jumlah):
        nilai = input(f"Nilai MK {i+1}: ").upper()
        if nilai == "A":
            total_nilai +=12
        elif nilai == "B":
            total_nilai += 9
        elif nilai == "C":
            total_nilai += 6
        elif nilai == "D":
            total_nilai += 3
        else:
            print("Nilai hanya bisa diinput A, B, C, atau D.")

    print("Nilai IPS Anda semester ini: ", round(total_nilai / total_sks, 2))

penghitung_IPS()