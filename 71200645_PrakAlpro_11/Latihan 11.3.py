def hitung_jam(filename):
    with open(filename, 'r') as file:
        jam_email = dict()

        for i in file:
            if i.startswith("From "):
                waktu = i.split()[5]
                jam = waktu.split(':')[0]
                jam_email[jam] = jam_email.get(jam, 0) + 1

    for jam, jumlah in sorted(jam_email.items()):
        print(jam, jumlah)

filename = ("mbox-short.txt")

hitung_jam(filename)
