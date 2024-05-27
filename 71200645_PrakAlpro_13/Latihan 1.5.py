# def faktorial(n):
#     if n == 0:
#         return 1
#     else:
#         return n * faktorial(n - 1)

# def kombinasi(n, r):
#     if r == 0 or r == n:
#         return 1
#     else:
#         return faktorial(n) // (faktorial(r) * faktorial(n - r))

# print(f"Kombinasi C({5}, {3}) = {kombinasi(5, 3)}")

def kombinasi(n, r):
    if r == 0 or r == n:
        return 1
    else:
        return kombinasi(n - 1, r - 1) + kombinasi(n - 1, r)

print(f"Kombinasi C({5}, {3}) = {kombinasi(5, 3)}")