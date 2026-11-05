total_hari_lembur = 0
tidak_lembur= 0
hari_lembur = 0
total_gaji = 0

for hari in range(1, 8):
    print("Hari ke-", hari)

    jam = int(input("Masukkan jam lembur: "))

    while jam < 0 or jam > 8 or jam == 5 or jam == 7:
        if jam == 0:
            pass
        elif jam > 8:
            print("Jam lembur melebihi batas!")
        else:
            print("Jam lembur tidak sesuai ketentuan!")

        jam = int(input("Masukkan ulang jam lembur: "))

    gaji = 100000

    lembur = jam * 25000 if jam >= 1 and jam<= 3 else 100000 if jam == 4 else 200000 if jam == 6 else 300000 if jam == 8 else 0

    if jam == 0 :
        continue
    else:
        shift = input("Apakah bekerja shift malam? (ya/tidak): ")

    if shift == "ya":
        gaji = gaji + 50000

    gaji = gaji + lembur
    total_gaji = total_gaji + gaji

    if jam > 0 and jam < 8 :
        hari_lembur += 1
    elif jam == 4:
        hari_lembur += 1
    elif jam == 6:
        hari_lembur += 1
    elif jam == 8:
        hari_lembur +=1
    else:
        tidak_lembur += 1

    total_hari_lembur
    if hari_lembur > tidak_lembur :
        total_hari_lembur = hari_lembur - tidak_lembur
    else:
        total_hari_lembur = 7 - tidak_lembur 


    print("Gaji hari ini: Rp", gaji)

print("=== RINGKASAN GAJI MINGGUAN ===")
print("total hari mengambil lembur:", total_hari_lembur, "hari")
print("Total gaji selama 7 hari: Rp", total_gaji)
print("===================================================")
