P = 200000000
r = 0.1
n = 1
A = 400000000
t = 0

while True:
    if P >= A:
        break
    else:
        P = P + (P * r)
        t = t + 1

print("Jumlah tahun: ", t)