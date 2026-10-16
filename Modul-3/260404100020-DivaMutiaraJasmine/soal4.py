penuh = 0

for i in range(1, 11):
    print("\nMahasiswa ke-", i)

    nama = input("Masukkan nama: ")
    ipk = float(input("Masukkan IPK: "))

    if ipk < 3.00:
        print("Tidak memenuhi syarat beasiswa")
        continue

    penghasilan = int(input("Penghasilan orang tua per bulan: Rp "))

    if penghasilan <= 3000000:
        if penuh < 3:
            status = "Beasiswa Penuh"
            penuh += 1
        else:
            status = "Kuota beasiswa penuh sudah habis"

    elif penghasilan <= 5000000:
        status = "Beasiswa Sebagian"

    else:
        status = "Tidak Mendapatkan Beasiswa"

    print("Nama:", nama)
    print("IPK:", ipk)
    print("Status:", status)

    if penuh == 3:
        print("Kuota beasiswa penuh sudah terpenuhi.")
        break

print("\nJumlah penerima beasiswa penuh:", penuh)


