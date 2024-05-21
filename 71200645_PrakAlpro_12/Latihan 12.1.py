n = int(input("Masukkan jumlah kategori: "))

data_aplikasi = {}
for i in range(n):
    nama_kategori = input("Masukkan nama kategori: ")
    print("Masukkan 5 nama aplikasi di kategori", nama_kategori)
    
    aplikasi = []
    for j in range(5):
        nama_aplikasi = input("Nama aplikasi: ")
        aplikasi.append(nama_aplikasi)
        
    data_aplikasi[nama_kategori] = aplikasi

print(data_aplikasi)

daftar_aplikasi_list = []
for aplikasi in data_aplikasi.values():
    daftar_aplikasi_list.append(set(aplikasi))
    
print(daftar_aplikasi_list)

hasil = daftar_aplikasi_list[0]
for i in range(1, len(daftar_aplikasi_list)):
    hasil = hasil.intersection(daftar_aplikasi_list[i])

print("Aplikasi yang muncul di semua kategori:", hasil)

# aplikasi yang hanya muncul di satu kategori
frekuensi_aplikasi = {}
for kategori in data_aplikasi.values():
    for aplikasi in kategori:
        if aplikasi in frekuensi_aplikasi:
            frekuensi_aplikasi[aplikasi] += 1
        else:
            frekuensi_aplikasi[aplikasi] = 1

unik_satu_kategori = {aplikasi for aplikasi, count in frekuensi_aplikasi.items() if count == 1}
print("Aplikasi yang hanya muncul di satu kategori:", unik_satu_kategori)

if n > 2:
    dua_kategori = {aplikasi for aplikasi, count in frekuensi_aplikasi.items() if count == 2}
    print("Aplikasi yang muncul tepat di dua kategori:", dua_kategori)