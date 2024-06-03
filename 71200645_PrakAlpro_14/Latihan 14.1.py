import re
from datetime import datetime

def selisih_tanggal(teks):
    tanggal = r"\d{4}-\d{2}-\d{2}"
    cari_tanggal = re.findall(tanggal, teks)
    
    tanggal_sekarang = datetime.now()
    
    hasil = []
    for i in cari_tanggal:
        ambil_tanggal = datetime.strptime(i, "%Y-%m-%d")
        selisih_hari = (tanggal_sekarang - ambil_tanggal).days
        
        ubah_bentuk = ambil_tanggal.strftime("%d-%m-%Y")
        # print(ubah_bentuk)
    
        hasil.append(f"{i} selisih {selisih_hari} hari")
    
    return hasil

teks = """
Pada tanggal 1945-08-17 Indonesia merdeka. Indonesia memiliki beberapa pahlawan
nasional, seperti Pangeran Diponegoro (TL: 1785-11-11), Pattimura (TL: 1783-06-08) dan Ki
Hajar Dewantara (1889-05-02).
"""

hasil_tanggal = selisih_tanggal(teks)
for i in hasil_tanggal:
    print(i)