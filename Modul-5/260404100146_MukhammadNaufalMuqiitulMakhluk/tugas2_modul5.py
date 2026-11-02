def palindrom(kata):
    if kata == kata[::-1]: #untuk membalikkan kata
        return True
    else:
        return False


kata = input("Masukkan sebuah kata: ")

hasil = palindrom(kata)

if hasil == True:
    print(kata, "adalah kata palindrom")
else:
    print(kata, "bukan kata palindrom")