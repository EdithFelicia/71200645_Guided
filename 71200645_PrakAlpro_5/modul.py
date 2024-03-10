kalimat = "Konversi yang sama"
panjang = len(kalimat)
for i in range(1, panjang):
    print(i, kalimat)
    
def konvergen(start):
    suku = start
    while suku != 1:
        print(suku)
        if suku % 2 == 0:
            suku = suku // 2
        else:
            suku = suku * 3 + 1
            
konvergen()

def average():
    total = 0
    count = 0
    while True:
        input_user = int(input("Masukkan nilai (nol atau negatif untuk berhenti): "))
        if input_user < 1:
            break
        else:
            total = total + input_user
            count = count + 1
    if count > 0:
        return total / count
    else:
        return 0
    
hasil = average()
print("Rata-rata: ", hasil)

for i in range(8, 101, 5):
    print(i)
    
for i in range(50, 1, -2):
    print(i)

for _ in range(1, 101):
    print(_, "Hello World")

ganjil = False
while ganjil == False:
    bilangan = int(input("Masukkan bilangan ganjil: "))
    if bilangan % 2 != 0:
        ganjil = True
print(bilangan, "yang anda masukkan adalah bilangan ganjil")

# printing the length of item in list
# for i in range(len(nilai)):
#     print(i)
    
# printing the value in list
# for i in nilai:
#   print(i)

nilai = [10, 99, 98, 85, 45, 59, 65, 66, 76, 12, 35, 13, 100, 80, 95]
my_message=""

length = len(nilai)

i = 0
while i < length:
    if nilai[i] == 100:
        my_message = f"There is a 100 at index no: {i}"
    i += 1
print(my_message)

for i in range(4, 24):
    if i == 19:
        break
    else:
        print(f"Halooo, no.{i}")
print("Finish!")