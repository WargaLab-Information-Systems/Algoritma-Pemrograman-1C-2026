
def palindrom(kata):
    kata = kata.lower()
    if kata == kata[::-1]:
        return True
    else:
        return False

kata = input("Masukkan sebuah kata: ")

hasil = palindrom(kata)

if hasil == True:
    print("Kata", kata, "merupakan kata palindrom")
else:
    print("Kata", kata, "bukan kata palindrom")
