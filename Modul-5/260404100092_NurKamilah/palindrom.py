def palindrom(kata):
    balik = ""

    for huruf in kata:
        balik = huruf + balik

    if kata == balik:
        return "Kata Palindrom"
    else:
        return "Bukan Kata Palindrom"


kata = input("Masukkan kata: ")

hasil = palindrom(kata)

print(hasil)