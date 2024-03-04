# def cek_digit_belakang(a, b, c):
#     a = a % 10
#     b = b % 10
#     c = c % 10
#     if a == b or b == c or a == c:
#         return True
#     return False

# print(cek_digit_belakang(30, 20, 18)) # True
# print(cek_digit_belakang(145, 5, 100)) # True
# print(cek_digit_belakang(71, 187, 18)) # False
# print(cek_digit_belakang(1024, 14, 94)) # True
# print(cek_digit_belakang(53, 8900, 658)) # False

def cek_digit_belakang2(a, b, c):
    a = str(a)
    b = str(b)
    c = str(c)
    if a[-1:] == b[-1:] or a[-1:] == c[-1:] or b[-1:] == c[-1:]:
        return True
    else:
        return False

print(cek_digit_belakang2(30, 20, 18)) # True
print(cek_digit_belakang2(145, 5, 100)) # True
print(cek_digit_belakang2(71, 187, 18)) # False
print(cek_digit_belakang2(1024, 14, 94)) # True
print(cek_digit_belakang2(53, 8900, 658)) # False

