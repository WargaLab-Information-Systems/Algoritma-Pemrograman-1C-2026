total_gaji = 0

for hari in range(1, 8):
    print(f"Hari ke-{hari}")

    while True:
        lembur = int(input("Jam lembur: "))
        if lembur < 0 or lembur == 5 or lembur == 7:
            print("Jam lembur tidak sesuai ketentuan, masukkan ulang.")
        else:
            break

    while True:
        shift = input("Shift malam (y/t): ")
        if shift == "y" or shift == "t":
            break
        print("Input tidak sesuai, masukkan y atau t.")

    if lembur == 0:
        upah_lembur = 0
    elif lembur <= 3:
        upah_lembur = lembur * 25000
    elif lembur == 4:
        upah_lembur = 100000
    elif lembur == 6:
        upah_lembur = 200000
    elif lembur == 8:
        upah_lembur = 300000
    else:
        print("Jumlah lembur melebihi batas yang ditentukan, upah lembur tidak dihitung.")
        upah_lembur = 0

    if shift == "y":
        tambahan_malam = 50000
    else:
        tambahan_malam = 0

    gaji_harian = 100000 + upah_lembur + tambahan_malam
    total_gaji += gaji_harian
    print(f"Gaji hari ke-{hari}: Rp{gaji_harian}")

print(f"Total gaji mingguan: Rp{total_gaji}")
