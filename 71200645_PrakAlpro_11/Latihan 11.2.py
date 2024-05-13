def data_diri(data):
    print("Data:", tuple(data))
    print()
    print("NIM :", data[1])
    print("NAMA :", data[0])
    print("ALAMAT :", data[2])
    print()

    nim = tuple(data[1])

    nama_depan = tuple(data[0].split()[0])
    nama_terbalik = ' '.join(data[0].split()[::-1])
    tuple_nama_terbalik = tuple(nama_terbalik.split())

    print(f"NIM: {nim}")
    print(f"NAMA DEPAN: {nama_depan}")
    print(f"NAMA TERBALIK: {tuple_nama_terbalik}")

daftar = ('Edith Felicia Putri', '71200645', 'Pekanbaru, Riau')

data_diri(daftar)
