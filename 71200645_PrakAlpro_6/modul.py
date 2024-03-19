# for i in range(5):
#     for j in range(2):
#         print("Hello, Moza")
#     print("Goodbye, Andra")
    
# Kolom itu pakai for loop outer
# Baris itu pakai for loop inner

# PRINT KE BAWAH
# for i in range(1, n + 1):
#     print(i)
    
# n = int(input("Masukkan n = ")) # 5
# for i in range(1, n + 1): # Perulangan 1 - 6
#     for j in range(1, i + 1): # i = 1, j = (1, 2)
#         print(i, " ", end="")
#     print()

# n = int(input("Masukkan n = ")) # 5
# for i in range(1, n + 1): # Perulangan 1 - 6
#     for j in range(1, i + 1): # i = 1, j = (1, 2)
#         print(j, " ", end="")
#     print()
    
# n = int(input("Masukkan n: "))
# i = n
# while i > 0:
#     j = i
#     while j > 0:
#         print(j, " ", end ="")
#         j -= 1
#     print("")
#     i -= 1

# n = int(input("Masukkan n: "))
# fokus ke inner loop
# for i in range(1, n + 1):
#     if i % 2 != 0: # ganjil
#         for j in range(1 , n + 1):
#             print(j, " ", end="")
#     else:
#         for j in range(n, 0, -1):
#             print(j, " ", end="")
#     print()
    
# Nggak semua WHILE bisa diubah ke for
# Semua FOR bisa diubah ke WHILE

# n = int(input("Masukkan n: "))
# for i in range(0, n + 1):
#     for j in range(1, n - i + 1):
#         if j % 2 == 1:
#             print("X", end="")

# def segitiga(jari_jari):
#     for i in range(1, jari_jari + 1):
#         print(" " * (jari_jari - i), end="")
#         print(" *" * i)
        
# segitiga(5)

# n = int(input("Masukkan n: "))
# for i in range(1, n):
#     print("" * (n - 1), "1 " * i)
# for j in range(n, 0, -1):
#     print("" * (n - 1), "* " * j)

# hasil = ""
# x = int(input("Masukkan jumlah: "))
# baris = x
# # Looping Baris
# while baris >= 0:
#     # Looping Kolom Spasi Kosong
#     kolom = baris
#     while kolom > 0:
#         hasil += "   "
#         kolom -= 1
    
#     # Looping Kolom Bintang
#     kanan = 1
#     while kanan < (x - (baris - 1)):
#         hasil += " * "
#         kanan += 1
    
#     hasil = hasil + "\n"
#     baris -= 1
# print(hasil)

# x = int(input("Masukkan bilangan 1 < x < 5: "))
# if 1 < x < 5:
#     if x == 2:
#         print("Angka kamu bagus sekali!")
# else:
#     print("Okaaay")

# x = int(input("Pilih angka dari 1 - 10: "))
# if x >= 1 and x <= 10:
#     if x == 5:
#         print("Angka yang kuinginkan")
#     else:
#         print("Bukan angka yang kuinginkan")
# else:
#     print("Anda salah memasukkan angka")

# print("Selamat datang di restoran!")
# x = input("Memulai pesan? y/n: ")
# if x == "y":
#     print("1. Keju Mozarella")
#     print("2. Hamburger")
#     pesanan = int(input("Masukkan angka pesanan Anda: "))
#     if pesanan == 1:
#         print("Terima kasih atas Keju Mozarellanya!")
#     elif pesanan == 2:
#         print("Terima kasih atas Hamburgernya!")
#     else:
#         print("Tidak ada menu yang lain")
# else:
#     if x == "n":
#         print("Terima kasih sudah mendatangi toko!")
#     else:
#         print("Anda salah memasukkan pilihan")

# x = int(input("Masukkan angka antara 1 - 10: "))
# if 1 <= x <= 10:
#     y = int(input("Masukkan angka antara 50 - 100: "))
#     if 50 <= y <= 100:
#         y = y + 50
#         print("nilai y:", y)
#     else:
#         if y > 100:
#             print("Nilai y sudah lebih dari 100:", y)
#         else:
#             print("Nilai y kurang dari 50:", y)
# else:
#     if x <= 0:
#         print("Nilai x memasukkin nilai negatif atau nol")
#     else:
#         print("Nilai x sudah lebih dari 10")

# print("Terima kasih sudah memasukkan angka")

# x = int(input("Masukkan angka antara 1 - 10: "))
# if 1 <= x <= 10:
#     if x < 8:
#         if x < 5:
#             if x == 2:
#                 print("Angka kesukaanku!")
# else:
#     print("Angka yang Anda masukkan salah")

# x = int(input("Masukkan angka: "))
# if x > 100:
#     print("Semakin tinggi")
# else:
#     if x < 0:
#         print("Sudah negatif")
#     else:
#         if 10 <= x <= 100:
#             print("Pertengahan")
#         else:
#             if x == 1:
#                 print("Hello 1")
#             else:
#                 print("Bukan yang pertama")