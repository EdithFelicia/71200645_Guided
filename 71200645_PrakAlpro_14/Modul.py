# import re
# RE.FINDALL
# pattern = r'\d+'
# text = 'The numbers are 12, 34, and 56.'

# matches = re.findall(pattern, text)
# print("Matches found:", matches)
# Kecocokan dikembalikan dalam bentuk list

# RE.FINDITER
# pattern = r'\d+'
# text = 'The numbers are 12, 34, and 56.'

# matches = re.finditer(pattern, text)
# for match in matches:
#     print("Match found:", match.group())

# RE.SUB
# pattern = r'\d+'
# replacement = '#'
# text = 'My phone number is 12345.'

# result = re.sub(pattern, replacement, text)
# print("Replaced text:", result)

# RE.FULLMATCH
# pattern = r'[a-zA-Z]+'
# text = 'Hello'

# match = re.fullmatch(pattern, text)
# if match:
#     print("Full match found:", match.group())
# else:
#     print("No full match")
    
# RE.SPLIT
# pattern = r'\s+'
# text = 'Split   this  sentence   into words.'

# result = re.split(pattern, text)
# print("Split text:", result)

# RE.COMPILE
# pattern = r'\d+'
# compiled_pattern = re.compile(pattern)

# text1 = 'There are 123 apples.'
# text2 = 'There are 456 oranges.'

# matches1 = compiled_pattern.findall(text1)
# matches2 = compiled_pattern.findall(text2)

# print("Matches in text1:", matches1)
# print("Matches in text2:", matches2)

# RE.ESCAPE
# text = 'This is a test. Use * and $ symbols.'
# escaped_text = re.escape(text)
# print("Escaped text:", escaped_text)


# import re

# def sensor_komentar(kalimat, terlarang, pengganti):
#     x = re.sub(terlarang, pengganti, kalimat)
#     return x

# kalimat = 'jancuk! aku dikibuli toko online.'
# terlarang = 'jancuk'
# pengganti = 'wkwkwk'
# print(sensor_komentar(kalimat, terlarang, pengganti))

import re

def validasi_kartu_kredit(nomor_kartu):
    if len(nomor_kartu) == 16:
        hasil = re.search("[^1237890]", nomor_kartu)
        huruf = re.search("[a-zA-Z]", nomor_kartu)
        if hasil and re.search("8888", nomor_kartu) and not huruf:
            return "Valid Platinum"
        if hasil and not huruf:
            return "Valid Reguler"
        else:
            return "Tidak valid"    
    else:
        return "Tidak valid"

nomor_kartu = '4234567888823456'
hasil = validasi_kartu_kredit(nomor_kartu)
print(hasil)

nomor_kartu = '42345678apa88823'
hasil = validasi_kartu_kredit(nomor_kartu)
print(hasil)

nomor_kartu = '411111111111111'
hasil = validasi_kartu_kredit(nomor_kartu)
print(hasil)

nomor_kartu = '811111111111111'
hasil = validasi_kartu_kredit(nomor_kartu)
print(hasil)

# baris ini jangan dihapus walaupun anda tidak menggunakan regex
# harus 16 digit angka
# harus diawali dengan 4/5/6
# jika ada angka 8 minimal 4 kali berdekatan, maka platinum
# tidak valid, reguler, platinum

       