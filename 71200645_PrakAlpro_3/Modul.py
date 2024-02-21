belanja = int(input("Pengeluaran: "))
voucher = 30 / 100
minimum = 100000
if belanja >= minimum:
    diskon = belanja * voucher
    print("Pengeluaran terbaru: ", belanja - diskon)
else:
    print("Pengeluaran: ", belanja)

pembelian = 120000
if pembelian >= 100000:
    print(True)
else:
    print(False)

True and True     # Hasil True
True and False    # Hasil False
False and False   # Hasil False
1 == 1 and 1 < 2  # Hasil True
1 < 2 and 3 < 1   # Hasil False
"Yes" and 100     # Hasil True

if "Besok hujan":
    print("Saya tidak kuliah")
elif "Saya menang game":
    print("Saya akan mentraktir teman")
elif "Saya menunggu di perpustakaan":
    print("Saya membaca buku")
else:
    print("Saya di rumah")

    usia = int(input("Usia user: "))
tinggi = int(input("Tinggi user: "))
pembelian = int(input("Pembelian: Rp."))
member = bool(input("Apakah Anda member? (True or False)" ))

if usia >= 10 and tinggi >= 100:
    print("Anda dapat menaiki wahana!")
if member == True or pembelian > 500000:
    print("Anda mendapat diskon!")

pembelian = int(input("Jumlah pembelian: "))
print("Diskon: ", round(0.1 * pembelian)) if pembelian > 100000 else 0

try:
    pembelian = int(input("Jumlah pembelian: "))
    if pembelian > 1000000:
        print("Anda mendapat diskon = 0.3") # diskon 30%
    elif pembelian > 500000 and pembelian <= 1000000:
        print("Anda mendapat diskon = 0.2") # diskon 20%
    elif pembelian >= 100000 and pembelian <= 500000:
        print("Anda mendapat diskon = 0.15") # diskon 15%
    else:
       print("Anda mendapat diskon = 0") # tidak ada diskon
except:
    print("Pembelian tidak sesuai")