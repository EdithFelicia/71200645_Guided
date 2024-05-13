# t1 = ("Kristus")
# print(type(t1))
# t2 = ("Yesus",)
# print(type(t2))

# elemen pada tuple tidak dapat berubah.
# tapi bisa diganti dengan elemen lain berdasarkan index

# tuple_1 = ()
# tuple_2 = tuple()


# kata = ("Akhir", "Zaman", "Tiba")
# print(kata[1])

# tuple_1 = "Yesus", "mengasihi", "kamu"
# tuple_2 = "selama", "lamanya"
# tuple_3 = (tuple_1, tuple_2)
# print(tuple_3)

# TIDAK BEKERJA
# t3 = tuple("dutawacana")
# t3[0] = "D"
# print(type(t3))
# print(t3)

# kata = tuple(["Beruang", "Kucing", "Panda", "Kupu-kupu"])
# kata = ("Penguin",) + kata[1:]
# print(kata)
# print(kata[0:1])
# print(kata[0:2])
# print(kata[1:3])
# print(kata[0:-1])
# print(kata[-1:-3])
# print(kata[-1:3])
# print(kata[-3:-1])

# a = (1, 2, 3)
# b = (50, 60, 70)
# c = a + b
# print(c)

# kalimat = 'but soft what light in yonder window breaks'
# dafkata = kalimat.split()
# t = list()
# for kata in dafkata:
#     t.append((len(kata), kata))

# t.sort(reverse=True)

# urutan = list()
# for length, kata in t:
#     urutan.append(kata)

# print(urutan)

# m = ["have", "fun"]
# x, y = m
# x = m[0]
# y = m[1]

# print(x)
# print(y)

# d = {"a": 10, "b": 1, "c": 22}
# t = list(d.items())
# print(t)

# kata = {"a": 10, "b": 1, "c": 22}
# daftar = list()
# for key, value in kata.items():
#     daftar.append((value, key))
# print(daftar)

# import string
# fhand = open("romeo-full.txt")
# counts = dict()
# for word in fhand:
#     line = line.translate(str.maketrans("","", string.punctuation))
#     line = line.lower()
#     words = line.split()
#     for word in words:
#         if word not in counts:
#             counts[word] = 1
#         else:
#             counts[word] += 1

# lst = list()
# for key, val in list(counts.items()):
#     lst.append((val, key))

# lst.sort(reverse=True)

# for key, val in lst[:]:
#     print(key, val)

# def nilai_rata_tertinggi(murid):
#     avg_tertinggi = 0
#     murid_tertinggi = None

#     for i in murid:
#         nama, nilai = i
#         avg = sum(nilai) / len(nilai)

#         if avg > avg_tertinggi:
#             avg_tertinggi= avg
#             murid_tertinggi = nama

#     return murid_tertinggi, avg_tertinggi

# murid = [("Yesaya", [85, 90, 92]), ("Yeremia", [78, 85, 80]), ("Yehezkiel", [90, 92, 95])]
# murid_tertinggi, avg_tertinggi = nilai_rata_tertinggi(murid)

# print("Nilai rata tertinggi")
# print("Nama:", murid_tertinggi)
# print("Nilai rata-rata:", avg_tertinggi)

# kata = ("Sampai jumpa", "saudaraku")
# pertama, kedua = kata
# print(pertama)
# print(kedua)

# kata = "Sampai jumpa", "saudaraku"
# (pertama, kedua) = kata
# print(pertama)
# print(kedua)

# kata = "Sampai jumpa", "saudaraku"
# pertama = kata[0]
# kedua = kata[1]
# print(pertama)
# print(kedua)

daftar = ("Dosa", "Dunia", 2000, 2024)
print(daftar)
del daftar

daftar = ("Hidup", "Suci", 2024)
print("Daftar baru:", daftar)