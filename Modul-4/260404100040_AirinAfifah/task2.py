total_gaji = 0
gaji = 100000
total_hari_lembur = 0

for i in range(1, 8):
    print(f"hari ke- {i}")

    jam_lembur = int(input("masukkan jam lembur: "))

    while jam_lembur < 0 or jam_lembur > 8:
        print("jumlah lembur melebihi batas")
        jam_lembur = int(input("masukkan ulang jam lembur: "))

    if jam_lembur > 0:
        total_hari_lembur +=1
    
    upah_lembur = jam_lembur * 25000 if jam_lembur >= 1 else jam_lembur <= 3   
    if jam_lembur == 4:
        upah_lembur = 100000
    elif jam_lembur == 5:
        upah_lembur = 150000
    elif jam_lembur == 6:
        upah_lembur = 200000
    elif jam_lembur == 7:
        upah_lembur = 250000
    elif jam_lembur == 8:
        upah_lembur = 300000
    else:
        upah_lembur = 0

    shift = input("Shift malam? (y/t): ")

    if shift == "y":
        tambahan_shift = 50000
    else:
        tambahan_shift = 0

    gaji_harian = gaji + upah_lembur + tambahan_shift
    total_gaji = total_gaji + gaji_harian

print(f"total hari lembur: {total_hari_lembur}")
print(f"Total gaji mingguan: {total_gaji}")
