jumlah_baris = int(input("jumlah baris lampu: "))
for baris in range(1, jumlah_baris + 1):
    jumlah_lampu = int(input(f"jumlah lampu pada baris {baris}: "))
    for lampu in range(1, jumlah_lampu + 1):
        if lampu % 3 == 0:
            print(f"baris{baris}, lampu {lampu}: mengalami gangguan")
        else:
            print(f"baris{baris}, lampu {lampu}: berfungsi normal")
print("periksa sumber listrik utama taman.")