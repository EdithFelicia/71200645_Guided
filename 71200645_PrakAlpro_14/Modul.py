import re
# RE.FINDALL
# pola = r"\d+"
# teks = "Sekarang umurmu sudah 21, ya! Sampai jumpa di tahun 2025"

# angka = re.findall(pola, teks)
# print("Angka:", angka)
# Kecocokan dikembalikan dalam bentuk list

# RE.FINDITER
# pola = r"\d+"
# teks = "Sekarang umurmu sudah 21, ya! Sampai jumpa di tahun 2025"

# angka = re.finditer(pola, teks)
# for i in angka:
#     print("Angka:", i.group())

# RE.SUB
# pola = r"\d+"
# pengganti = "Sampai jumpa!"
# teks = "Jangan lupa telepon, ya! 56486032"

# hasil = re.sub(pola, pengganti, teks)
# print("Kata-kata terakhir:", hasil)

# RE.FULLMATCH
# pola = r"[a-zA-Z]+"
# teks = "Hello"

# hasil = re.fullmatch(pola, teks)
# if hasil:
#     print("sesuai:", hasil.group())
# else:
#     print("Tidak ada yang sama")
    
# RE.SPLIT
# pola = r"\s+"
# teks = "Aku   melihat Surga   terbuka  dan Anak Allah   duduk di sebelah   kanan Bapa."

# hasil = re.split(pola, teks)
# print("Kata terpisah:", hasil)

# RE.COMPILE
# pola = r"\d+"
# kompilasi_pola = re.compile(pola)

# teks1 = "Pola yang sama dalam 2 teks"
# teks2 = "Hello angka 3126, selamat pagi!"

# sama1 = kompilasi_pola.findall(teks1)
# sama2 = kompilasi_pola.findall(teks2)

# print("Kesamaan pola teks1:", sama1)
# print("Kesamaan pola teks2:", sama2)

# RE.ESCAPE
# teks = "Menambahkan simbol \ pada kata sebelum spasi dalam teks"
# tambah_escaped = re.escape(teks)
# print("Escaped teks:", tambah_escaped)
       