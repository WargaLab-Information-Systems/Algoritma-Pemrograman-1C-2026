def cek_palindrom(kata):
    panjang = len(kata)
    
    for i in range(int(panjang / 2)):
        if kata[i] != kata[panjang - 1 - i]:
            return False
            
    return True

kata = input("Masukkan sebuah kata: ")

if cek_palindrom(kata) == True:
    print("Ini polindrom")
else:
    print("Ini bukan polindrom")

print(cek_palindrom(kata))
    