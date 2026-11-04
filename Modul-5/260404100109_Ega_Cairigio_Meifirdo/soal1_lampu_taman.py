baris = int(input("Masukkan jumlah baris lampu: "))
jumlah_lampu = int(input("Masukkan jumlah lampu pada setiap baris: "))

for z in range(1, baris + 1):
    print(f"Baris ke-{z}")
    for s in range(1, jumlah_lampu + 1):
        if s % 3 == 0:
            print(f"  Lampu {s}: mengalami gangguan")
        else:
            print(f"  Lampu {s}: berfungsi normal")

print("Periksa sumber listrik utama taman.")
