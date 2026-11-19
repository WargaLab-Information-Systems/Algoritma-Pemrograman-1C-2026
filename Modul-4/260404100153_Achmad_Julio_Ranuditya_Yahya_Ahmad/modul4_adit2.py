total_gaji = 0

for hari in range(1, 8):
    print("\nHari ke-", hari)

    lembur = int(input("Masukkan jam lembur (0-8): "))

    while lembur < 0 or lembur == 5 or lembur == 7 or lembur > 8:
        print("Jam lembur tidak sesuai ketentuan!")
        lembur = int(input("Masukkan ulang jam lembur: "))

    shift = input("Apakah bekerja shift malam? (ya/tidak): ")

    gaji = 100000

    if lembur >= 1 and lembur <= 3:
        gaji += lembur * 25000
    elif lembur == 4:
        gaji += 100000
    elif lembur == 6:
        gaji += 200000
    elif lembur == 8:
        gaji += 300000

    if shift.lower() == "ya":
        gaji += 50000

    total_gaji += gaji

    print("Gaji hari ke-", hari, "adalah Rp", gaji)

print("\nTotal gaji mingguan: Rp", total_gaji)