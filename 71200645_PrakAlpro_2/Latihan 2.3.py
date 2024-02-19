# Kerja Budi selama 5 minggu
# Gaji dihitung per jam.

gaji_perjam = int(input("Total gaji per jam: Rp."))
jumlah_jamKerja = int(input("Total jam dalam seminggu: "))

print("")

pendapatan = gaji_perjam * (jumlah_jamKerja * 5)
print("Pendapatan Budi sebelum pajak: Rp.", pendapatan)

total_pajak = 14/100 * pendapatan
pendapatan_bersih = pendapatan - total_pajak
print("Pendapatan Budi setelah pajak: Rp.", pendapatan_bersih)

beli_baju_aksesoris = 10/100 * pendapatan_bersih 
print("Jumlah uang yang akan Budi habiskan untuk membeli pakaian dan aksesoris: Rp.", beli_baju_aksesoris)

beli_alat_tulis = 1/100 * pendapatan_bersih
print("Jumlah uang yang akan Budi habiskan untuk membeli alat tulis: Rp.", beli_alat_tulis)

sisa = pendapatan_bersih - (beli_alat_tulis + beli_baju_aksesoris)
sedekah = 25/100 * sisa
print("Jumlah uang yang akan Budi sedekahkan: Rp.", sedekah)

anak_yatim = 30/100 * sedekah
print("Jumlah uang yang akan diterima anak yatim: Rp.", anak_yatim)
sisa_dari_sedekah = sedekah - anak_yatim
print("Jumlah uang yang akan diterima kaum dhuafa: Rp.", sisa_dari_sedekah)
