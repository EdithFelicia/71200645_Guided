# python hanya bisa membaca file txt dengan r.

handle = open('File/mbox-short.txt', 'r')
print(handle)
handle.close()

#####################

handle = open('File/mbox-short.txt')
count = 0
for line in handle:
    count = count + 1
print('Line Count:', count)
handle.close()

######################

handle = open("File/Kawan.txt", "w")
handle.write("Jesus Christ")
handle.write(" Raja di atas segala raja")
handle.close()

with open("File/Kawan.txt", "r") as file:
    ganti_kata = file.read().replace("Raja", "Tuan")
    with open("File/Kawan.txt", "w") as file_2:
        file_2.write(ganti_kata)

with open("File/mbox-short.txt","r") as file:
    for i in file:
        if i.startswith("Received") and count <=10:
            print(f"{count}.\t{i}")
            count += 1

#####################
            
handle = open("File/mbox-short.txt", "r")
for i in handle:
    count = 0
    if i.startswith("Subject:") and count < 10:
        count += 1
        print(i.strip().title())
print(f"Ada {count} baris")

handle.close()

#####################

try:
    nama = input("Nama file: ")
    handle = open(nama, "r")
    total_byte = 0
    for i in handle:
        total_byte += len(i.strip())
    print(f"{total_byte/1000} KB")
except:
    print("File tidak ditemukan")

# Ukuran byte mungkin tidak tepat karena ada spasi atau tidak ada spasi, enter atau tidak ada enter