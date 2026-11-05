total_gaji = 0

for hari in range(1, 8):
    print(f"hari ke - {hari}")

    jam_lembur = int(input("masukkan jam lembur:"))

    while jam_lembur < 0 or jam_lembur > 8:
        print("jam lembur tidak sesuai ketentuan!")
        jam_lembur = int(input("masukkan ulang jam lembur:"))

    shift = input("shift (siang/malam): ")

    gaji = 100000

    if jam_lembur >= 1 and jam_lembur <= 3:
        gaji += jam_lembur * 25000
    elif jam_lembur == 4:
        gaji += 100000
    elif jam_lembur == 6:
        gaji += 200000
    elif jam_lembur == 8:
        gaji += 300000

    if shift == "malam":
        gaji += 50000

    total_gaji += gaji

    print("gaji hari ini: Rp", gaji)

print("total gaji selama 7 hari: Rp", total_gaji)