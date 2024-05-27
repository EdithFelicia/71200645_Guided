def palindrom(kalimat):
    kalimat = ''.join(i.lower() for i in kalimat if i.isalnum())
    
    if len(kalimat) <= 1:
        return True
    if kalimat[0] != kalimat[-1]:
        return False
    return palindrom(kalimat[1:-1]) 

kalimat = "nama Ibu ini Ubiaman"
if palindrom(kalimat):
    print("Kalimat tersebut adalah palindrom.")
else:
    print("Kalimat tersebut bukan palindrom.")