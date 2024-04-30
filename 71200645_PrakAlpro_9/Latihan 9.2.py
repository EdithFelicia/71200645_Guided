def simpan_user():
    nilai = []
    while True:
        angka = input("Masukkan angka atau ketik 'done' untuk selesai: ")
                
        if angka.lower() == "done":
            break
        
        try:
            daftar_nilai = float(angka)  # Coba konversi masukan ke float
            nilai.append(daftar_nilai)  # Tambahkan angka ke dalam list
        except ValueError:
            print("Angka tidak valid, coba lagi")
            
    if nilai:  # Periksa apakah list tidak kosong
        nilai_max = int(max(nilai))  # Cari nilai maksimum
        nilai_min = int(min(nilai))  # Cari nilai minimum
        print("Nilai maksimum adalah:", nilai_max)
        print("Nilai minimum adalah:", nilai_min)
    else:
        print("Tidak ada angka yang dimasukkan.")

simpan_user()