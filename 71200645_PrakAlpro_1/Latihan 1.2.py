jumlah_emas = 25
harga_emas = 650000
harga_beli = jumlah_emas * harga_emas

harga_emas_baru = 685000
harga_jual = jumlah_emas * harga_emas_baru
untung = harga_jual - harga_beli
persentase_untung_jual = (untung/harga_beli) * 100
print("Keuntungan Gerard (dalam Rp dan dalam %): Rp", untung, "dan", persentase_untung_jual,"%")

beli_lagi = 15
harga_beli_kedua = beli_lagi * harga_emas_baru
harga_keseluruhan_beli = harga_beli_kedua + harga_beli

total_emas = jumlah_emas + beli_lagi
kenaikan_harga = 715000
harga_jual_kedua = total_emas * kenaikan_harga
untung_jual_kedua = harga_jual_kedua - harga_keseluruhan_beli
persentase_untung_jual_kedua = (untung_jual_kedua/harga_keseluruhan_beli) * 100
print("Keuntungan Gerard (dalam Rp dan dalam %): Rp", untung_jual_kedua, "dan", persentase_untung_jual_kedua,"%")