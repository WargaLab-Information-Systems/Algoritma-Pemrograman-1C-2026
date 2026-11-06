baris = int(input("Masukkan jumlah baris lampu: "))
lampu = int(input("Masukkan jumlah lampu setiap baris: "))

for i in range(1, baris + 1):
    print(f"\nBaris {i}")
    for j in range(1, lampu + 1):
        if j % 3 == 0:
            print(f"  Lampu {j}: mengalami gangguan")
        else:
            print(f"  Lampu {j}: berfungsi normal")

print("\nSeluruh lampu telah diperiksa. Silakan periksa sumber listrik utama taman.")