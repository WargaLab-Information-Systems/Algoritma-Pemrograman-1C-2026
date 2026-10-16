
jumlah = 0
pendapatan = 0
total_jarak = 0
jarak_terjauh = 0

while True:
    jarak = float(input("Masukkan jarak penumpang (0 untuk selesai): "))

    if jarak == 0:
        break

    if jarak < 0:
        print("Jarak tidak valid, masukkan ulang!")
        continue

    jumlah += 1
    total_jarak += jarak

    if jarak <= 5:
        tarif = 3000
    elif jarak <= 15:
        tarif = 3000 + (jarak - 5) * 1000
    else:
        tarif = 13000 + (jarak - 15) * 500

    if jumlah % 5 == 0:
        tarif = tarif * 50 / 100
        print("Mendapat diskon 50%")

    pendapatan += tarif

    if jarak > jarak_terjauh:
        jarak_terjauh = jarak

    print("Tarif:", tarif)

if jumlah > 0:
    rata_rata = total_jarak / jumlah
else:
    rata_rata = 0

print("\nJumlah penumpang:", jumlah)
print("Total pendapatan: Rp", pendapatan)
print("Jarak terjauh:", jarak_terjauh, "km")
print("Rata-rata jarak:", rata_rata, "km") 