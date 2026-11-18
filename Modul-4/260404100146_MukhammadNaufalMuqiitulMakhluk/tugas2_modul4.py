total_gaji = 0

for hari in range(1, 8):
    print("\nHari ke-", hari)

    lembur = int(input("Masukkan jam lembur (0-8): "))

    while lembur < 0 or lembur > 8 or lembur == 5 or lembur == 7:
        print("Jam lembur tidak sesuai ketentuan!")
        lembur = int(input("Masukkan ulang jam lembur: "))

    shift = input("Apakah bekerja shift malam? (y/n): ")

    gaji = 100000

    if lembur >= 1 and lembur <= 3:
        upah_lembur = lembur * 25000
    elif lembur == 4:
        upah_lembur = 100000
    elif lembur == 6:
        upah_lembur = 200000
    elif lembur == 8:
        upah_lembur = 300000
    else:
        upah_lembur = 0

    if shift == "y":
        tambahan_malam = 50000
    else:
        tambahan_malam = 0

    gaji_harian = gaji + upah_lembur + tambahan_malam
    total_gaji = total_gaji + gaji_harian

    print("Gaji hari ini: Rp", gaji_harian)

print("\nTotal gaji selama seminggu: Rp", total_gaji)