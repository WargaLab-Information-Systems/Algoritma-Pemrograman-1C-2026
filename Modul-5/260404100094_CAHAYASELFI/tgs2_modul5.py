def cek_palindrom(kata):
    kata_balik = kata [::-1]
    return kata == kata_balik

kata_input = input("Masukkan kata: ")
hasil = cek_palindrom(kata_input)

print("Apakah palindrom?", hasil)
if hasil:
    print("Kata tersebut adalah palindrom!")
else:
    print("Kata tersebut bukan palindrom.")