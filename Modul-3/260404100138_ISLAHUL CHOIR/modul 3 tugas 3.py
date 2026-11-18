
jumlah_A = 0
jumlah_B = 0
jumlah_C = 0
jumlah_D = 0
jumlah_E = 0
total = 0

tertinggi = -1
terendah = 101

for i in range(1,11):
    print("\nMahasiswa ke-", i)

    nama = input("Nama: ")
    tugas = float(input("Nilai tugas: "))
    uts = float(input("Nilai UTS: "))
    uas = float(input("Nilai UAS: "))

    akhir = tugas * 0.3 + uts * 0.3 + uas * 0.4
    total+=akhir

    if akhir >= 85:
        kategori = "A"
        jumlah_A = jumlah_A + 1
    elif akhir >= 75:
        kategori = "B"
        jumlah_B = jumlah_B + 1
    elif akhir >= 65:
        kategori = "C"
        jumlah_C = jumlah_C + 1
    elif akhir >= 50:
        kategori = "D"
        jumlah_D = jumlah_D + 1
    else:
        kategori = "E"
        jumlah_E = jumlah_E + 1

    print("Nama:", nama)
    print("Nilai Tugas:",tugas)
    print("Nilai UTS:",uts)
    print("Nilai UAS:",uas)
    print("Nilai akhir:",akhir)
    print("Kategori Nilai:", kategori)

    if akhir > tertinggi:
        tertinggi = akhir
        nama_tertinggi = nama

    if akhir < terendah:
        terendah = akhir
        nama_terendah = nama
rata_rata = total/10

print("\nJumlah A:", jumlah_A)
print("Jumlah B:", jumlah_B)
print("Jumlah C:", jumlah_C)
print("Jumlah D:", jumlah_D)
print("Jumlah E:", jumlah_E)

print("Nilai tertinggi:", tertinggi)
print("Nama:", nama_tertinggi)
print("Nilai terendah:", terendah)
print("Nama:", nama_terendah)
print("Rata-rata Nilai akhir:",rata_rata )
