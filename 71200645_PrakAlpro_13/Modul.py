# from numpy import prod
# from itertools import permutations

# # menggunakan library
# def permutasi(m,n):
#     return prod(range(m, 1, -1)) / prod(range(m-n, 1, -1))

# print(permutasi(10, 4))
# print(len(list(permutations(range(10), 4))))

# menghitung rekursif manual
# def permutasi_manual(m, n):
#     if (n == 0):
#         return 1
#     else:
#         return (permutasi_manual(m, n-1) * (m-n+1))

# print(permutasi_manual(10, 4))

# x = 3
# total = x
# for i in range(3):
#     if i == 2:
#         print(i)
#         print(f"{x-i} ", end="")
#         break
#     print(f"{x-i} + ", end="")
#     total += i
# print(f"= {total}")

# def soal_1(x, y):
#     if y == 1:
#         print(f"{x} = ", end="")
#         return x
#     else:
#         print(f"{x} + ", end="")
#         return x + soal_1(x, y-1) # memanggil fungsi lagi
# print(soal_1(2,4))

# def faktorial(n):
#     if n == 0 or n == 1:
#         return 1
#     else:
#         return faktorial(n-1) * n
# print(faktorial(4))

# def halo():
#     print("Hello World")
#     halo()
    
# halo() # error karena perulangan terlalu banyak dan tidak ada tanda-tanda akan berhenti

# def fibo(n):
#     if n == 1:
#         return [1]
#     elif n == 2:
#         return [1,1]
#     else:
#         call = fibo(n - 1)
#         call.append(call[-1] + call[-2])
#         return call

# print(fibo(6))

# def power(n, pangkat):
#     if pangkat == 1:
#         print(f"{n} = ", end="")
#         return n
#     elif pangkat == 0:
#         return 1
#     else:
#         print(f"{n} * ", end="")
#         return n * power(n, pangkat - 1)

# print(power(2, 4))

# def konversi(angka, basis):
#     biner = "0123456789ABCDEF"
#     if angka < basis:
#         return biner[angka]
#     else:
#         return konversi(angka//basis, basis) + biner[angka%basis]
    
# print(konversi(8, 2))
# print(konversi(10, 16))

# def tampil_angka(i):
#     print(f"Perulangan ke {i}")

# tampil_angka(4)

# def faktorial(n):
#     if n == 0:
#         return 1
#     else:
#         return n * faktorial(n - 1)

# def permutasi(n, r):
#     return faktorial(n) // faktorial(n - r)

# print(f"Permutasi P({10}, {4}) = {permutasi(10, 4)}")

# def perulangan(angka):
#     if angka > 1:
#         print(angka, end="")
#         angka -= 1
#         perulangan(angka)
#     else:
#         print(angka)
        
# pengguna = int(input("Masukkan angka:"))
# perulangan(pengguna)

# def tampilkanAngka (batas, i = 1):
#   print(f'Perulangan ke {i}')

#   if (i < batas):
#     # di sini lah rekursifitas itu terjadi
#     tampilkanAngka(batas, i + 1)

# # memanggil fungsi tampilkanAngka
# # untuk pertama  kali
# tampilkanAngka(10)

def deret_ganjil(n):
    if n == 1:
        return 1
    else:
        return (n - 1) * 4 + deret_ganjil(n - 1)

n = 6  # Jumlah suku deret yang ingin dihitung
hasil = deret_ganjil(n)
print(f"Jumlah deret ganjil dari 1 + 3 + 7 + 11 + 15 + ... + {n} adalah {hasil}.")