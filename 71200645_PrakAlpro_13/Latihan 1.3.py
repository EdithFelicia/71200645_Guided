def deret_ganjil(n):
    if n == 1:
        return 1
    elif n % 2 == 0:
        n -= 1
    return n + deret_ganjil(n - 2)

print(f"Jumlah deret ganjil adalah {deret_ganjil(9)}")