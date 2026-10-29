total = 0

for hari in range(1, 8):
    print("Hari ke-", hari)

    lembur = int(input("Jam lembur: "))
    while lembur in(5, 7) or lembur < 0:
        lembur = int(input("Tidak sesuai, masukkan ulang: "))

    if lembur == 0:
        upah = 0
    elif lembur <= 3:
        upah = lembur * 25000
    elif lembur == 4:
        upah = 100000
    elif lembur == 6:
        upah = 200000
    elif lembur == 8:
        upah = 300000
    else:
        print("Lembur melebihi batas, tidak dihitung upah lembur")
        upah = 0

    malam = input("Shift malam? (y/t): ")
    if malam == "y":
        upah = upah + 50000
    total = total + 100000 + upah

print("Total gaji: ", total)