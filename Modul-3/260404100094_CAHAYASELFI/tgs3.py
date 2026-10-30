print("=== PENGELOLA NILAI MAHASISWA ===")

jumlah_a = 0
jumlah_b = 0
jumlah_c = 0
jumlah_d = 0
jumlah_e = 0

total_nilai_kelas = 0
nilai_tertinggi = -1
nama_tertinggi = ""
nilai_terendah = 101
nama_terendah = ""

for i in range(1, 11):
    print("\nData Mahasiswa ke-", i)
    nama = input("Nama: ")
    tugas = float(input("Nilai Tugas (0-100): "))
    uts = float(input("Nilai UTS (0-100): "))
    uas = float(input("Nilai UAS (0-100): "))
    
    nilai_akhir = (0.3 * tugas) + (0.3 * uts) + (0.4 * uas)
    print("Nilai Akhir:", nilai_akhir)
    
    if nilai_akhir >= 85:
        kat = "A"
        jumlah_a = jumlah_a + 1
    elif nilai_akhir >= 75:
        kat = "B"
        jumlah_b = jumlah_b + 1
    elif nilai_akhir >= 65:
        kat = "C"
        jumlah_c = jumlah_c + 1
    elif nilai_akhir >= 50:
        kat = "D"
        jumlah_d = jumlah_d + 1
    else:
        kat = "E"
        jumlah_e = jumlah_e + 1
        
    print("Kategori:", kat)
    
    total_nilai_kelas = total_nilai_kelas + nilai_akhir
    
    if nilai_akhir > nilai_tertinggi:
        nilai_tertinggi = nilai_akhir
        nama_tertinggi = nama
        
    if nilai_akhir < nilai_terendah:
        nilai_terendah = nilai_akhir
        nama_terendah = nama

rata_rata_kelas = total_nilai_kelas / 10

print("=== RINGKASAN KELAS ===")
print("Jumlah Kategori A :", jumlah_a)
print("Jumlah Kategori B :", jumlah_b)
print("Jumlah Kategori C :", jumlah_c)
print("Jumlah Kategori D :", jumlah_d)
print("Jumlah Kategori E :", jumlah_e)
print("Nilai Tertinggi   :", nilai_tertinggi, "(", nama_tertinggi, ")")
print("Nilai Terendah    :", nilai_terendah, "(", nama_terendah, ")")
print("Rata-rata Kelas   :", rata_rata_kelas)