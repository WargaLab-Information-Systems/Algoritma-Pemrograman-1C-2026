#Brankas
kode = int(input("Masukkan kode 3 digit: "))
d1 = kode // 100
d2 = kode // 10 % 10
d3 = kode % 10
print("digit pertama: ", d1)
print("digit kedua: ", d2)
print("digit ketiga: ", d3)

pelacak = d1 * d3
print("Nilai pelacak awal: ", pelacak)

if d2 % 2 == 1:
    pelacak = pelacak + 25 
else: 
    pelacak = pelacak - d2
    print("Nilai pelacak tahap pertama: ", pelacak)

if pelacak % 3 == 0:
    pelacak = pelacak // 3
else:
    pelacak = pelacak * 2
    print("Nilai pelacak tahap kedua (nilai akhir): ", pelacak)

if pelacak > 50:
    print("Password Kategori A")
elif pelacak > 20:
    print("Password Kategori B")
else:
    print("Password ditolak")

if pelacak % 2 == 0:
    print("Siklus Genap")
else:
    print("Siklus Ganjil")