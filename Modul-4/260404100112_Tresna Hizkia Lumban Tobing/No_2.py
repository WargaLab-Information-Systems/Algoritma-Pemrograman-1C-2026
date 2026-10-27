total_gaji = 0
for hari in range(1, 8):
    print("\nHari ke-", hari)
    lembur = int(input("Masukkan jam lembur: "))
    while lembur not in [0, 1, 2, 3, 4, 6, 8]:
        if lembur > 8:
            print("Jumlah lembur melebihi batas yang ditentukan!")
        else:
            print("Jam lembur tidak sesuai ketentuan!")
        lembur = int(input("Masukkan ulang jam lembur: "))
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
    shift = input("Shift malam? (ya/tidak): ")
    gaji_harian = 100000 + upah_lembur
    if shift == "ya":
        gaji_harian = gaji_harian + 50000
    total_gaji = total_gaji + gaji_harian
    print("Gaji hari ini: Rp", gaji_harian)
print("\nTotal gaji mingguan: Rp", total_gaji)
