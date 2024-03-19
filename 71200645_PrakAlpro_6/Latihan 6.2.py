def deret_bilangan():
    nilai = int(input("Masukkan nilai n = "))
    jumlah = 1
    for i in range (nilai): # untuk buat baris
        for j in range(nilai, 0, -1): # Nilai nol tidak termasuk, jadi berhenti di-1
            jumlah = jumlah * j # untuk buat perkalian (6 x 5 x 4 x 3 x 2 x 1)
        print(jumlah, end=" ")
        for k in range(nilai, 0, -1):
            print(k, end=" ") # Untuk buat deretan (6, 5, 4, 3, 2, 1) # menyamping
        jumlah = 1 # Untuk me-reset nilai variable hitung
        nilai -= 1
        print()

deret_bilangan() 