# Soal 2 - Gaji Mingguan Karyawan

total_gaji = 0 

for hari in range(1, 8):
    print("\n=== Hari ke-", hari, "===")

    while True:
        lembur = int(input("Masukkan jam lembur: "))
        if lembur > 8:
            print("Jumlah lembur melebihi batas yang ditentukan!")
        elif lembur == 0 or lembur == 1 or lembur == 2 or lembur == 3 or lembur == 4 or lembur == 6 or lembur == 8:
            break
        else:
            print("Jam lembur tidak sesuai ketentuan, input ulang!")

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

    shift = input("Apakah shift malam? (y/t): ")
    if shift == "y":
        tambahan = 50000
    else:
        tambahan = 0

    gaji_hari = 100000 + upah_lembur + tambahan
    print("Gaji hari ini: Rp", gaji_hari)
    total_gaji = total_gaji + gaji_hari

print("\nTotal gaji seminggu: Rp", total_gaji)