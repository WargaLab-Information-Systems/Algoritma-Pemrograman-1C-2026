baris = int(input("masukkan jumlah baris lampu: "))
jumlah_lampu = int(input("masukkan jumlah lampu setiap baris: "))

for i in range(1, baris + 1):
    print(f"baris ke- {i}")
    for j in range(1, jumlah_lampu + 1):
        if j % 3 == 0:
            print(f"lampu {j}:", "mengalami gangguan")
        else:
            print(f"lampu {j}:", "berfungsi normal")

print("memeriksa sumber listrik utama taman")