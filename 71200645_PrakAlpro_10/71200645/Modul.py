# eng2sp = {'one': 'uno', 'two': 'dos', 'three': 'tres'}
# print('one' in eng2sp) # True
# print(eng2sp['one']) # uno
# Pemanggilan dict hanya bisa menggunakan key.

# a = dict()
# a['ken']=['bakso','nasgor']
# a['ivan']=['teman']
# a['ivanz']=[43]
# print(a)

# word = "Hello Friends"
# d = dict()
# for i in word:
#     if i not in d:
#         d[i] = 1 # buat dict baru
#     else:
#         d[i] += 1

# print(d)

# counts = {"chuck":1, "annie":42, "jan":100}
# print(counts.get("doni")) #default isinya 0.
# bisa pula nilai default diletakkan di dalam. ("doni", 0)


# fname = input("Enter the file name: ")
# try:
#     fhand = open(fname)
# except:
#     print("File cannot be opened:", fname)
#     exit()

# counts = dict()
# for line in fhand:
#     words = line.split()
#     for word in words:
#         if word not in counts:
#             counts[word] = 1
#         else:
#             counts[word] += 1
# print(counts)

# a = dict()
# for i in range(3):
#     var = dict()
#     var['nama'] = input('masukkan nama anda: ')
#     var['noHP'] = int(input('masukkan nomor hp anda: '))
#     nim = int(input("masukkan NIM anda: "))
#     a[nim] = var
# print(a)

counts = {"chuck":1, "annie":42, "jan":100, "rudi": 0}
for i in counts:
    if counts[i] > 10:
        print(i, counts[i])

# dict = {"Tuhan": "Yesus", "Dosa": "Maut"}

# my_God = dict["Tuhan"]
# print(my_God)  # Output: Yesus

# dict["Imam"] = "Eli"

# dict["Nabi"] = "Elia"

# del dict["Imam"]
# dict.pop("Dosa")

# for key, value in dict.items():
#     print(f"{key}: {value}")

# def tambah_kontak(buku_telepon, nama, nomor):
#     buku_telepon[nama] = nomor
#     print(f"Kontak {nama} ditambah/perbaharui.")

# def hapus_kontak(buku_telepon, nama):
#     if nama in buku_telepon:
#         del buku_telepon[nama]
#         print(f"Kontak {nama} dihapus.")
#     else:
#         print(f"Kontak {nama} tidak ditemukan.")

# def cari_kontak(buku_telepon, nama):
#     return buku_telepon.get(nama, "Kontak tidak ditemukan.")

# buku_telepon = {}
# tambah_kontak(buku_telepon, 'Erwin', '0570-0000-911')
# tambah_kontak(buku_telepon, 'Levi', '(03)5285-8181')
# print(cari_kontak(buku_telepon, 'Eren'))
# hapus_kontak(buku_telepon, 'Erwin')

# keys = ['Izuku', 'Uraraka', 'Iida']
# values = ['Deku', 'Uravity', 'Ingenium']
# hero = dict(zip(keys, values))
# print(hero)

# print(hero.get('Deku'))

# keys = ['Izuku', 'Uraraka', 'Iida']
# values = ['Deku', 'Uravity', 'Ingenium']

# my_hero = {}
# for i in range(len(keys)):
#     my_hero[keys[i]] = values[i]
    
# print(my_hero)