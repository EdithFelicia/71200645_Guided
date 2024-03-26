# Bro has gain the type of "I see you from the distance without seeing you"
# "Just from my side eye", "Just like how I know Angelo is there"


# namasaya = "Antonius Rachmat C"
# temansaya1 = "Yuan Lukito"
# temansaya2 = 'Laurentius Kuncoro'
# temansaya3 = "Matahari" + 'Bakti'

# print(temansaya3)
# print(namasaya[0]) #'A'
# print(namasaya[9]) #'R'
# print(temansaya1[1]) #'u'

# huruf = temansaya2[0]
# print(huruf) #'L'

# # Spasi dihitung sebagai karakter

# kalimat = input("kalimat = ")
# for kal in kalimat:
#     print(kal)
# # membuat barisan deretan kalimat per karakter

# kalimat = "cerita rakyat"
# awal = 0
# akhir = 7
# print(kalimat[awal:akhir])
# print(kalimat[:5]) # 0 - 5

kalimat = "Satu Bangsa"
kalimat_baru = kalimat[0:5] + "Allah"
print(kalimat_baru) #Satu Allah

# kalimat = "Fans Hololive, pada tanggal 16-03-2024 ada festival ke-5!"
# hasil = kalimat.split(" ")
# print(hasil)
# for i in hasil:
#     if i[0].isdigit(): # kata yang dimulai dengan angka
#         print(i)
#         hasil_2 = i.split("-")
#         print(hasil_2)
#         print(hasil_2[1] + "/" + hasil_2[0] + "/" + hasil_2[2])

# def kata_hidup():
#     kalimat = input("Masukkan kalimat: ").lower()
#     jumlah = 0
#     for i in "aiueo": # yang di-looping adalah string "aiueo-nya"
#         hasil = kalimat.count(i)
#         jumlah = hasil + jumlah
#     print("Jumlah huruf hidup:",jumlah)
        
# kata_hidup()

#####################

# satu = "Step! on, no... pets??"
# satu = satu.lower()

# cara elegan
# satu = "".join([i for i in satu if i.isalpha()])
# print(satu)

# satu_baru =""
# for i in satu:
#     if i.isalpha():
#         satu_baru += i

# dua = satu_baru[::-1]
# if dua == satu_baru:
#     print("Palindrom")
# else:
#     print("bukan")

text = "A quick brown fox jumps over the lazy dog.".lower()
def ambil_kata_kalimat(kalimat, n):
    kalimat = kalimat.lower()
    print(kalimat)
    hasil_akhir = []
    hasil = kalimat.split()
    print(hasil)
    for i in range(0, len(hasil)):
        tmp = " ".join(hasil[i:i + n])