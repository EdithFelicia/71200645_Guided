def tanya_jawab():
    with open("Latihan 8.2/soal.txt", "r") as file:
        hasil = file.readlines()
        
        for i in hasil:
            soal, jawaban = i.strip().split("||")
            print(soal.strip())
            jawaban_pengguna = input("jawab: ").strip().lower()
            
            if jawaban_pengguna == jawaban.strip().lower():
                print("Jawaban benar!")
            else:
                print("Jawaban salah!")
        
tanya_jawab()