try:
    suhu = int(input("Masukkan suhu tubuh: "))
    if suhu >= 38:
        print("Anda demam")
    elif suhu <= 37:
        print("Anda tidak demam")
except:
    print("Anda salah memasukkan input suhu")
