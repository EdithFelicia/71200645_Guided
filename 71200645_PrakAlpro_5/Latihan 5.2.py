# Deret bilangan ganjil dari batas bawah dan batas atas pengguna.
# batas atas < batas bawah => Dimulai dari batas atas

def ganjil():
    bawah = int(input("Masukkan bilangan batas bawah: "))
    atas = int(input("Masukkan bilangan batas atas: "))
    
    if atas < bawah:
        for i in range(bawah, atas - 1, -1):
            if i % 2 != 0:
                print(i,end="." if atas+1 == i or atas == i else ", ")
        
    elif atas > bawah:
        for i in range(bawah, atas + 1):
            if i % 2 != 0:
                print(i,end="." if atas-1 == i or atas == i else ", ")
     

ganjil()