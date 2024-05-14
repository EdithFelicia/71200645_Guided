def hitung_jam(filename):
    with open(filename, 'r') as file:
        jam_email = []

        for i in file:
            if i.startswith("From "):
                waktu = i.split()[5]
                jam = waktu.split(':')[0]
                jam_email.append((jam, 1))

    hitung_email = {}
    for jam, _ in jam_email:
        hitung_email[jam] = hitung_email.get(jam, 0) + 1

    jam_email_tuple = list(hitung_email.items())
    jam_email_tuple.sort()

    for jam, jumlah in jam_email_tuple:
        print(jam, jumlah)

filename = "mbox-short.txt"
hitung_jam(filename)