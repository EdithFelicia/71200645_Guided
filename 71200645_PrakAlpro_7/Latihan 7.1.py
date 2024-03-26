def is_anagram():
    kata_1 = input("Masukkan kata pertama: ").lower()
    kata_2 = input("Masukkan kata kedua: ").lower()

    urut_kata_1 = sorted(kata_1)
    urut_kata_2 = sorted(kata_2)

    if urut_kata_1 == urut_kata_2:
        print(f"{kata_1} dan {kata_2} adalah anagram.")
    else:
        print(f"{kata_1} dan {kata_2} bukan anagram.")
        
is_anagram()