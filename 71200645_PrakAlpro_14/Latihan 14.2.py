import re
import random
import string

def buat_password(length = 8):
    karakter= string.ascii_letters + string.digits
    password = ""
    for i in range(length):
        password += random.choice(karakter)
    return password

def ambil_user_dan_beri_password(teks):
    pola_email = r"[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}"
    email = re.findall(pola_email, teks)
    
    hasil = []
    for i in email:
        username = i.split("@")[0]
        password = buat_password()
        hasil.append(f"{i} username: {username}, password: {password}")
    return hasil

teks = """
Berikut adalah daftar email dan nama pengguna dari mailing list:
anton@mail.com dimiliki oleh antonius
budi@gmail.co.id dimiliki oleh budi anwari
slamet@getnada.com dimiliki oleh slamet slumut
matahari@tokopedia.com dimiliki oleh toko matahari
"""

hasil = ambil_user_dan_beri_password(teks)
for i in hasil:
    print(i)