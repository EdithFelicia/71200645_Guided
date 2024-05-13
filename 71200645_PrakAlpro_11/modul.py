# t1 = ("a")
# t2 = "a"
# print(t1)
# t3 = tuple()
# print(t3)

# elemen pada tuple tidak dapat berubah.
# tapi bisa diganti dengan elemen lain berdasarkan index

# TIDAK BEKERJA
# t3 = tuple("dutawacana")
# t3[0] = "D"
# print(type(t3))
# print(t3)

# t3 = tuple("dutawacana")
# t3 = ("D",) + t3[1:]
# print(t3)

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

# d = {"a": 10, "b": 1, "c": 22}
# t = list()
# for key, val in d.items():
#     t.append((val, key))
# print(t)

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

