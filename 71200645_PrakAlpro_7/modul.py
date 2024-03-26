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

# kalimat = "Satu Bangsa"
# kalimat_baru = kalimat[0:5] + "Allah"
# print(kalimat_baru) #Satu Allah

# kalimat = "Fans Hololive, pada tanggal 16-03-2024 ada festival ke-5!"
# hasil = kalimat.split()
# for i in hasil:
#     if i[0].isdigit(): #kata yang dimulai dengan angka
#         print(i)
#         hasil_2 = i.split("-")
#         print(hasil_2)
#         print(hasil_2[0] + "/" + hasil_2[1] + "/" + hasil_2[2]) #urutan pada list

# def kata_hidup():
#     kalimat = input("Masukkan kalimat: ").lower()
#     jumlah = 0
#     huruf_hidup = "aiueo"
#     for i in huruf_hidup: # yang di-looping adalah string "aiueo-nya"
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

# text = "A quick brown fox jumps over the lazy dog.".lower()
# def ambil_kata_kalimat(kalimat, n):
#     kalimat = kalimat.lower()
#     print(kalimat)
#     hasil_akhir = []
#     hasil = kalimat.split()
#     print(hasil)
#     for i in range(0, len(hasil)):
#         tmp = " ".join(hasil[i:i + n])

# kalimat = "Dia pengikut Kristus"
# data = "pengikut"
# print(data in kalimat)      #True
# print("Kristus" in kalimat) #True
# print("Farisi" in kalimat)  #False

# if "Barnabas" > "Yesus":
#     print("Rakyat minta bebaskan!")
# else:
#     print("Cari cara lain!")
    
# kalimat = "Pada mulanya adalah Firman; Firman itu bersama-sama dengan Allah dan Firman itu adalah Allah"
# print(len(kalimat))

# terakhir = kalimat[len(kalimat)-1]
# terakhir_2 = kalimat[-1]
# print(f"{terakhir} dan {terakhir_2} sama")

# kalimat = "Mata Tuhan ada di segala tempat, mengawasi orang jahat dan orang baik"
# i = 0
# while i < len(kalimat):
#     print(kalimat[i], end="")
#     i += 1

# kalimat = "Segala perkara dapat kutanggung di dalam Dia yang memberi kekuatan kepadaku"
# for i in kalimat:
#     print(i, end="")

# kata_1 = "saya"
# kata_2 = "dibasuh"
# kata_3 = kata_1 + " " + kata_2 + " bersih "

# kata_4 = "selamanya "
# print(kata_3 + kata_4 * 7)

# Menghilangkan karakter dari index ganjil
# def string_ganjil():
#     kata = input("Masukkan kata: ")
#     hasil = ""
    
#     for i in range(len(kata)):
#         if i % 2 == 0:
#             hasil = hasil + kata[i]
    
#     print(hasil)

winter_trees_lines = ['All the complicated details', 'of the attiring and', 'the disattiring are completed!', 'A liquid moon', 'moves gently among', 'the long branches.', 'Thus having prepared their buds', 'against a sure winter', 'the wise trees', 'stand sleeping in the cold.']

winter_trees_full = ("\n".join(winter_trees_lines))
print(winter_trees_full)