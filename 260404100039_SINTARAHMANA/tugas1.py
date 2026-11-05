jumlah_baris = int(input("masukkan jumlah baris lampu:"))
jumlah_lampu = int(input("masukkan jumlah lampu setiap baris:"))

for baris in range(1, jumlah_baris + 1):
    print(f"baris ke - {baris}")

    for lampu in range(1, jumlah_lampu + 1):
        if lampu % 3 == 0:
            print(f"lampu {lampu}: mengalami gangguan")
        else:
            print(f"lampu {lampu}: berfungsi normal")

print("periksa sumber listrik utama taman!")
