nama_file = input("Masukkan nama file: ")  

def hitung_kemunculan_email(nama_file):
    kemunculan_email = {}

    with open(nama_file, 'r') as file:
        for baris in file:
            if baris.startswith('From '):
                kata = baris.split()
                email = kata[1]
                if email in kemunculan_email:
                    kemunculan_email[email] += 1
                else:
                    kemunculan_email[email] = 1

    return kemunculan_email

hasil = hitung_kemunculan_email(nama_file)
print(hasil)