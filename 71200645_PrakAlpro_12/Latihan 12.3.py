def kata():
    try:
        nama_file1 = input("Masukkan nama file pertama: ")
        nama_file2 = input("Masukkan nama file kedua: ")

        with open(nama_file1, 'r') as file1:
            kata_set1 = set(file1.read().lower().split())

        with open(nama_file2, 'r') as file2:
            kata_set2 = set(file2.read().lower().split())

        # Mencari kata yang muncul di kedua file
        kata_sama = kata_set1.intersection(kata_set2)
        print("Kata-kata yang muncul di kedua file: ")
        for i in sorted(kata_sama):
            print(i)

    except FileNotFoundError as e:
        print(f"Error: File tidak ditemukan - {e}")
    except Exception as e:
        print(f"Error: Terjadi kesalahan - {e}")

kata()