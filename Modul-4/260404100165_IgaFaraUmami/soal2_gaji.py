total_gaji = 0

for hari in range(1, 8):
    print("\nHari ke-", hari)

    while True:
        lembur = int(input("Masukkan jam lembur (0-8): "))
        if 0 <= lembur <= 8:
            break
        else:
            print("Jam lembur melebihi batas atau tidak valid! Masukkan ulang.")

    if lembur <= 3:
        upah_lembur = lembur * 25000
    elif lembur == 4:
        upah_lembur = 100000
    elif lembur == 6:
        upah_lembur = 200000
    elif lembur == 8:
        upah_lembur = 300000
    else:
        upah_lembur = 0

    shift = input("Apakah shift malam? (y/n): ")
    if shift == "y":
        upah_shift = 50000
    else:
        upah_shift = 0

    gaji_harian = 100000 + upah_lembur + upah_shift
    total_gaji += gaji_harian
    print("Gaji hari ke-", hari, ": Rp", gaji_harian)
print("\nTotal gaji selama 7 hari: Rp", total_gaji)