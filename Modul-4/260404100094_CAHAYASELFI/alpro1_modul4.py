# Soal 1 - Pemeriksaan Lampu Taman Kota

baris = int(input("Masukkan jumlah baris lampu: "))
lampu = int(input("Masukkan jumlah lampu setiap baris: "))

for i in range(1, baris + 1):
    print("\nBaris ke-", i)
    for j in range(1, lampu + 1):
        if j % 3 == 0:
            print("Lampu", j, "mengalami gangguan")
        else:
            print("Lampu", j, "berfungsi normal")

print("\nSilakan periksa sumber listrik utama taman!")