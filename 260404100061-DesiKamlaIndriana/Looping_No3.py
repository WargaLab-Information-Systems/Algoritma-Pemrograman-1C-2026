print("=== Sistem Penilaian dan Kelulusan Mahasiswa ===")
Total_seluruh_mahasiswa = 10
Jumlah_mahasiswa_kategoriA = 0
Jumlah_mahasiswa_kategoriB = 0
Jumlah_mahasiswa_kategoriC = 0
Jumlah_mahasiswa_kategoriD = 0
Jumlah_mahasiswa_kategoriE = 0
Nilai_tertinggi = 0
Nama_tertinggi = 0
Nilai_terendah = 100
Nama_terendah = 0
Total_seluruh_nilai = 0
for i in range(10):
    Nama_peserta = (input("Nama_peserta = "))
    Nilai_tugas = int(input("Nilai_tugas = "))
    Nilai_UTS = int(input("Nilai_UTS = "))
    Nilai_UAS = int(input("Nilai_UAS = "))
    Bobot_Nilai_tugas = 30 / 100
    Bobot_Nilai_UTS = 30 / 100
    Bobot_Nilai_UAS = 40 / 100
    Nilai_akhir = (Nilai_tugas * Bobot_Nilai_tugas ) + (Nilai_UTS * Bobot_Nilai_UTS) + (Nilai_UAS * Bobot_Nilai_UAS)
    print("Nilai_akhir =", Nilai_akhir)
    if Nilai_akhir >= 85:
        print("Kategori = A")
        Jumlah_mahasiswa_kategoriA = Jumlah_mahasiswa_kategoriA + 1
        print("Jumlah Mahasiswa Kategori A = ", Jumlah_mahasiswa_kategoriA)
    elif Nilai_akhir >= 75:
        print("Kategori = B")
        Jumlah_mahasiswa_kategoriB = Jumlah_mahasiswa_kategoriB + 1
        print("Jumlah Mahasiswa Kategori B = ", Jumlah_mahasiswa_kategoriB) 
    elif Nilai_akhir >= 65:
        print("Kategori = C")
        Jumlah_mahasiswa_kategoriC = Jumlah_mahasiswa_kategoriC + 1
        print("Jumlah Mahasiswa Kategori C = ", Jumlah_mahasiswa_kategoriC)
    elif Nilai_akhir >= 50:
        print("Kategori = D") 
        Jumlah_mahasiswa_kategoriD = Jumlah_mahasiswa_kategoriD + 1
        print("Jumlah Mahasiswa Kategori D = ", Jumlah_mahasiswa_kategoriD) 
    else:
        print("Kategori = E")
        Jumlah_mahasiswa_kategoriE = Jumlah_mahasiswa_kategoriE + 1
        print("Jumlah Mahasiswa Kategori E = ", Jumlah_mahasiswa_kategoriE) 
    if Nilai_akhir > Nilai_tertinggi:
        Nilai_tertinggi = Nilai_akhir
        Nama_tertinggi = Nama_peserta
    if Nilai_akhir < Nilai_terendah:
        Nilai_terendah = Nilai_akhir
        Nama_terendah = Nama_peserta
    Total_seluruh_nilai = Total_seluruh_nilai + Nilai_akhir
  
print("Nilai tertinggi = ", Nilai_tertinggi)
print("Nama tertinggi = ", Nama_tertinggi)
print("Nilai terendah = ", Nilai_terendah)
print("Nama terendah = ", Nama_terendah)
print("Total seluruh nilai = ", Total_seluruh_nilai)
Rata_rata_nilai = Total_seluruh_nilai / Total_seluruh_mahasiswa
print("Rata-rata nilai = ", Rata_rata_nilai)
