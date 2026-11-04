def luas_persegi_panjang (panjang, lebar):
    luas = panjang * lebar
    return luas

p = int(input("Masukkan panjang:"))
l = int(input("Masukkan lebar:"))

hasil = luas_persegi_panjang(p,l)
print("Luas persegi panjang adalah:", hasil)


luas_persegi = lambda sisi: sisi * sisi

s = int(input("Masukkan panjang sisi: "))

hasil = luas_persegi(s)

print("Luas persegi adalah:", hasil)

