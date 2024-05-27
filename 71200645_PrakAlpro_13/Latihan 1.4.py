def jumlah_angka(n):
    if n < 10:
        return n
    else:
        return n % 10 + jumlah_angka(n // 10)

print("Hasil =", jumlah_angka(234))

# print(234 % 10) # 4
# print(234 // 10) # 23
# 23 > 10, sehingga rekursif lagi
# print(23 % 10) # 3
# print(23 // 10) # 2
# Hasil 4 + 3 + 2 = 9