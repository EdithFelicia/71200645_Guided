def tiga_terbaik(nilai):
    urutan = sorted(nilai) # Merapikan dari rendah ke tinggi
    urutan.reverse() # Urutan dari tinggi ke rendah
    print(urutan[:3]) # Mengambil 3 nilai tertinggi
    
tiga_terbaik([100, 35, 76, 93, 81, 22, 40, 55])