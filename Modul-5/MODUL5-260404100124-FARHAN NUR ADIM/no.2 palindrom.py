kata = str(input("Masukkan sebuah kata: "))

def palindrom (kata):
    if kata == kata[::-1]:
        return True
    else:
        return False

hasil = palindrom(kata)

if hasil == True:
    print (kata, "merupakan kata palindrom")
else:
    print (kata, "bukan kata palindrom")