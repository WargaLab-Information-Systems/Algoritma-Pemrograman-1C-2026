jumlah_beasiswa_penuh = 0

for i in range(1, 11):
    if jumlah_beasiswa_penuh == 3:
        print("\nKuota beasiswa penuh sudah terpenuhi!")
        break

    print("\nMahasiswa ke-", i)

    nama = input("Masukkan nama mahasiswa: ")
    ipk = float(input("Masukkan IPK: "))

    if ipk < 3.00:
        print("Tidak memenuhi syarat beasiswa.")
        continue

    penghasilan = int(input("Masukkan penghasilan orang tua per bulan: Rp"))

    if penghasilan <= 3000000:
        status = "Beasiswa Penuh"
        jumlah_beasiswa_penuh = jumlah_beasiswa_penuh + 1
    elif penghasilan <= 5000000:
        status = "Beasiswa Sebagian"
    else:
        status = "Tidak Mendapatkan Beasiswa"

    print("Nama:", nama)
    print("IPK:", ipk)
    print("Penghasilan orang tua: Rp", penghasilan)
    print("Hasil seleksi:", status)

print("\n===== HASIL AKHIR SELEKSI =====")
print("Jumlah penerima beasiswa penuh:", jumlah_beasiswa_penuh)