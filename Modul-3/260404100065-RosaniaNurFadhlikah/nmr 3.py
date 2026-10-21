nama1 = ""
akhir1 = 0
nama_tertinggi = ""
nilai_tertinggi = 0
nama_terendah = ""
nilai_terendah = 100

jumlah_a = 0
jumlah_b = 0
jumlah_c = 0
jumlah_d = 0
jumlah_e = 0
total_akhir = 0

for i in range(10):
    print("Mahasiswa ke", i+1)
    nama = input("Nama: ")
    tugas = float(input("Tugas: "))
    uts = float(input("UTS: "))
    uas = float(input("UAS: "))

    akhir = tugas*0.3 + uts*0.3 + uas*0.4
    total_akhir = total_akhir + akhir

    if akhir >= 85:
        kat = "A"
        jumlah_a = jumlah_a + 1
    elif akhir >= 75:
        kat = "B"
        jumlah_b = jumlah_b + 1
    elif akhir >= 65:
        kat = "C"
        jumlah_c = jumlah_c + 1
    elif akhir >= 50:
        kat = "D"
        jumlah_d = jumlah_d + 1
    else:
        kat = "E"
        jumlah_e = jumlah_e + 1

    print(nama, "nilai akhir", akhir, "kategori", kat)
    print("")

    
    if i == 0:
        nilai_tertinggi = akhir
        nilai_terendah = akhir
        nama_tertinggi = nama
        nama_terendah = nama
    else:
        if akhir > nilai_tertinggi:
            nilai_tertinggi = akhir
            nama_tertinggi = nama
        if akhir < nilai_terendah:
            nilai_terendah = akhir
            nama_terendah = nama

print("Jumlah A:", jumlah_a)
print("Jumlah B:", jumlah_b)
print("Jumlah C:", jumlah_c)
print("Jumlah D:", jumlah_d)
print("Jumlah E:", jumlah_e)
print("Tertinggi:", nama_tertinggi, nilai_tertinggi)
print("Terendah:", nama_terendah, nilai_terendah)
print("Rata-rata:", total_akhir/10)