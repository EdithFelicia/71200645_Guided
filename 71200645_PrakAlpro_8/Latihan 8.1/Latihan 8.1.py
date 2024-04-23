def perbandingan_file():
    file_1 = "Latihan 8.1/teks_1.txt"
    file_2 = "Latihan 8.1/teks_2.txt"
    
    with open(file_1, 'r') as f1, open(file_2, 'r') as f2:
        f1_lines = f1.readlines()
        f2_lines = f2.readlines()

    max_lines = max(len(f1_lines), len(f2_lines))

    for i in range(max_lines):
        if i < len(f1_lines) and i < len(f2_lines):
            if f1_lines[i] != f2_lines[i]:
                print(f"Perbedaan di baris ke-{i + 1}:")
                print(f"File 1: {f1_lines[i].strip()}")
                print(f"File 2: {f2_lines[i].strip()}")
                print()
        elif i < len(f1_lines):
            print(f"Perbedaan di baris ke-{i+1}:")
            print(f"File 1: {f1_lines[i].strip()}")
            print()
            
        elif i < len(f2_lines):
            print(f"Perbedaan di baris ke-{i+1}:")
            print(f"File 2: {f2_lines[i].strip()}")
            print()
            
perbandingan_file()
