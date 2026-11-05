def cek_palindrom(kata):
    if kata == kata[::-1]:
        return True
    else:
        return False
    
kata = input("Masukkan sebuah kata: ")
hasil = cek_palindrom(kata)

if hasil == True:
    print("Kata tersebut adalah palindrom")
else:
    print("Kata tersebut bukan palindrom")