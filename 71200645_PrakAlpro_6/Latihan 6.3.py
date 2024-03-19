def deret_bilangan() : 
    tinggi = int(input("Masukkan tinggi = "))
    lebar = int(input("Masukkan lebar = "))
    deret = 1
    for i in range (tinggi) : 
        for j in range (lebar) :
            print(deret,end=" ")
            deret += 1
        print()
    

deret_bilangan()