def cek_palindrom(kata):
    kata = kata.lower()
    if kata == kata[::-1]:
       return True
    else:
       return False

kata = input("Masukkan kata : ")
hasil = cek_palindrom(kata)
print("Nilai kembalian fungsi :", hasil)
if hasil:
    print("Kata", kata, "merupakan palindrom")
else:
    print("Kata", kata, "bukan palindrom")
