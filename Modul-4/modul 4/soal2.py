total = 0 
jumlah_lembur = 0 

for h in range(1, 8):
    print(f"\nHari ke-{h}")
    shift = input("kerja shift malam? (ya/tidak): ").lower()

    while True:
        lembur = int(input("jam lembur (0, 1, 2, 3, 4, 6, 8): "))

        if lembur in [0, 1, 2, 3, 4, 6, 8]:
            break
        else:
            print("Input tidak valid, masukkan ulang!")

    upah_lembur = (0 if lembur == 0 or lembur > 8 else
        lembur * 25000 if 1 <= lembur <= 3 else
        100000 if lembur == 4 else
        200000 if lembur == 6 else
        300000 if lembur == 8 else
        0)

    if lembur > 0:
        jumlah_lembur += 1

    gaji = 100000
    
    if shift == 'ya':
        gaji += 50000
        
    gaji += upah_lembur
    total += gaji
    
    print(f"Gaji hari ke-{h}: Rp {gaji:,}")

print(f"Total Gaji Mingguan: Rp {total:,}")
print(f"Total hari mengambil lembur: {jumlah_lembur:,}kali ")