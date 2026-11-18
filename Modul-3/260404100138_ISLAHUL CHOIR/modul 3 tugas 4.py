
penuh = 0

for i in range(1,11):
    print("\nMahasiswa ke-", i + 1)

    nama = input("Nama: ")
    ipk = float(input("IPK: "))

    if ipk < 3.00:
        print("Tidak memenuhi syarat")
        continue

    penghasilan = int(input("Penghasilan orang tua: "))

    if penghasilan <= 3000000:
        if penuh < 3:
            print("Mendapat beasiswa penuh")
            penuh = penuh + 1
        else:
            print("Kuota beasiswa penuh habis")

    elif penghasilan <= 5000000:
        print("Mendapat beasiswa sebagian")

    else:
        print("Tidak mendapat beasiswa")

    if penuh == 3:
        print("Kuota beasiswa penuh terpenuhi")
        break

print("Jumlah penerima beasiswa penuh:", penuh)
