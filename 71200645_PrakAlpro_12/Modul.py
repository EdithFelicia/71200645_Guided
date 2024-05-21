# def unique_sum(list):
#     set_tanpa_duplikat = set(list)
#     hasil = 0
#     for i in set_tanpa_duplikat:
#         hasil += i
        
#     return hasil

# x = [2, 4, 3, 2, 7, 8, 6, 4, 5, 5]
# hasil = unique_sum(x)
# print(f"Total penjumlahan: {hasil}")

# def cek_duplikat(string):
#     set_karakter = set()
    
#     for i in string:
#         if i in set_karakter:
#             return True
#         else:
#             set_karakter.add(i)
    
#     return False

# cek_duplikat('angka')
# cek_duplikat('dan')

# n = int(input("Masukkan jumlah kategori: "))
# aplikasi = {}
# for i in range(n):
#     kategori = str(input(f"Masukkan nama kategori ke-{i+1}: "))
#     set_app = set()
#     for j in range(5):
#         input_app = str(input(f"Masukkan nama aplikasi ke-{j+1}: "))
#         set_app.add(input_app)
#     aplikasi[kategori] = set_app

# list_kategori = []
# for kategori in aplikasi:
#     list_kategori.append(aplikasi[kategori])

# hasil = list_kategori[0]
# for i in range(1, len(list_kategori)):
#     hasil = hasil.intersection(list_kategori[i])
    
# print(hasil)

# nim = {'71200120', '71200195', '71200214'}
# jumlah_nim = len(nim)
# print(jumlah_nim) # akan menghasilkan output 3
# # tampilkan isi set satu-persatu
# for n in nim:
#     print(n)

# # definisikan sebuah set kosong
# plat_nomor = set()
# # tambahkan plat nomor 'AB 1890 XA'
# plat_nomor.add('AB 1890 XA')
# # tambahkan plat nomor 'AD 6810 MT'
# plat_nomor.add('AD 6810 MT')
# # jumlah anggota di dalam Set
# print(len(plat_nomor))
# # tambahkan plat yang sama sekali lagi
# plat_nomor.add('AB 1890 XA')
# # tampilkan semua plat nomor
# for plat in plat_nomor:
#     print(plat)

# set_1 = {}
# set_2 = set()

# kata = {"Alfa", "Omega", "Datang"}
# print(type(kata))
# print(kata)
# print(kata[1]) # error: tidak bisa diakses lewat index

# kata = set(["Kasih", "Yesus", "Selamanya"])
# print(type(kata))

# kata2 = set(("Hidup", "Kekal", "Surga"))
# print(type(kata2))



# def hitung_daerah(daftar):
#     daerah_unik = set(daftar)  # Mengubah list menjadi set untuk menghapus duplikasi
#     jumlah_daerah = len(daerah_unik)  # Menghitung jumlah daerah unik
#     return daerah_unik, jumlah_daerah

# daftar = ["Jakarta", "Bandung", "Surabaya", "Jakarta", "Medan", "Bandung", "Bali", "Surabaya", "Bali", "Makassar"]
# daerah_unik, jumlah_daerah = hitung_daerah(daftar)
# print("Daerah yang diwakili:", daerah_unik)
# print("Jumlah daerah:", jumlah_daerah)

