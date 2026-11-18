baris = int(input("Masukkan jumlah baris lampu: "))
lampu = int(input("Masukkan jumlah lampu setiap baris: "))

for i in range(1, baris + 1):
    print("\nBaris ke-", i)

    for j in range(1, lampu + 1):
        if j % 3 == 0:
            print("Lampu", j, ": Mengalami gangguan")
        else:
            print("Lampu", j, ": Berfungsi normal")

print("\nPeriksa sumber listrik utama taman!")