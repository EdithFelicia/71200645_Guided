list = [1, 2, 3, 4]
print(f"Nama: {list}")

ulang = [0, 1, 2] * 3
print(ulang)

akses = ["b", "a", "c", "e"]
print(akses[0]) # b
print(akses[-1]) # e
print(akses[2]) # c

satu = []
satu.append(1)

satust = [1,2,3]
duast = [4,5,6]
tigast = [7,8,9]
satust.extend(duast)
satust.extend(tigast)
print(satust)
print(satust+duast+tigast)

angka = [0,1,2,3,4,5]
angka.pop(3)
print(angka)

angka2 = angka.copy()
del angka2[2]
print(angka2)
# pop sama del, fungsinya sama
# del tidak bisa digunakan di dalam variabel sementara pop bisa.

terpop = angka.pop(3)
# terdelete = del angka2

# remove => hanya menghapus satu elemen yang ditemui lebih dulu.
angka_1 = [1,2,3,4,5,4]
angka_1.remove(4)
print(angka_1) # 4 di akhir masih ada di dalam list.

# How to remove all the same item
# Pakai looping
angka_angka = [1,2,3,4,5,3,7,5,3]
for i in range(angka_angka.count(3)):
    angka_angka.remove(3)
    
print(angka_angka)

list1 = []
for i in range(4):
    # list1.append(i)
    list1.insert(0,i)
print(list1)

list_1 = [1,2,3]
list_1.reverse() # method yang pakai . (kalau tidak ada return, nilainya void)
list_2 = reversed(list_1) # mengembalikan dalam bentuk objek
print(list_1)
print(list_2)

listt = [1,2,3]
listtt = listt[::-1]
print(listtt)

a = "ini ada14h string"
b = ["ini", "ada", 1, 4, "string"]
print(id(b))
b[0] = 100
print(id(b))

def hapus_index_pertama(list):
    return list[1:]

list1 = [1,2,3,4]
print(hapus_index_pertama(list1))

def elemen_sama(list1, list2):
    for x in list1:
        for y in list2:
            if x == y:
                return True
    return False

print(elemen_sama([1,2,3], [3,4,5]))

def terbesar_kedua(listnya):
    listnya.sort()
    print(listnya)
    
    list2 = []
    for i in listnya:
        if i not in list2:
            list2.append(i)
    print(list2)
    print(list2[-2])

terbesar_kedua([1,2,3,4,5,6,8,9,9,3,4,5,7])

def apakahsublist(A, B):
    sub_set = False
    if B == []:
        sub_set = True
    elif B == A:
        sub_set = True
    elif len(B) > len(A):
        sub_set = False
    else:
        for n in B:
            if n not in A:
                break
            else:
                sub_set= True
    return sub_set

a = [2,4,3,5,7]
b = [4,7]
c = [3, 7, 5, 2, 4]
print(apakahsublist(a, b))
print(apakahsublist(a, c))

                    

