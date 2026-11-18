total_gaji = 0

for hari in range(1, 8):
    print(f"\nHari ke-{hari}")

    while True:
        lembur = int(input("Masukkan jam lembur (0-8): "))

        if 0 <= lembur <= 8:
            break
        else:
            print("Jam lembur tidak valid! Masukkan ulang antara 0-8 jam.")

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

    shift = input("Apakah bekerja shift malam? (ya/tidak): ").lower()

    if shift == "ya":
        tambahan_malam = 50000
    else:
        tambahan_malam = 0

    gaji_harian = 100000 + upah_lembur + tambahan_malam

    print(f"Gaji hari ke-{hari}: Rp{gaji_harian:,}".replace(",", "."))

    total_gaji += gaji_harian

print("\n==============================")
print("Total gaji mingguan: Rp" +
      format(total_gaji, ",").replace(",", "."))
print("==============================")