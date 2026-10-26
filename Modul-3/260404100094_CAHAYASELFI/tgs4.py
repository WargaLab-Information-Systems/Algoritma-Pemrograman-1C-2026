penuh = 0

for i in range(10):
    print("\nMahasiswa ke-", i + 1)
    nama = input("Masukkan nama: ")
    ipk = float(input("Masukkan ipk: "))
    gaji = int(input("Masukkan penghasilan orang tua: "))

    if ipk < 3.00:
        print(nama, "- Tidak memenuhi syarat IPK")
        continue

    if gaji <= 3000000:
        print(nama, "- Beasiswa penuh")
        penuh += 1
    elif gaji <= 5000000:
        print(nama, "- Beasiswa sebagian")
    else:
        print(nama, "- Tidak mendapat beasiswa")

    if penuh == 3:
        print("Kuota beasiswa penuh sudah terpenuhi, seleksi dihentikan.")
        break

print("Jumlah penerima beasiswa penuh:", penuh)