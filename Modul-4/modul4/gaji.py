total_gaji=0
gaji_pokok=100000
lembur=0
hari=0
for hari in range(1, 8):
    print(f"\nhari ke-{hari}")
    while True:
        lembur=int(input("masukkan jam lembur (0-8):"))
        if lembur in{0, 1, 2, 3, 4, 6, 8}:
            break
        else:
            print("jam lembur tidak sesuai ketentuan!")
            print("masukkan 0, 1, 2, 3, 4, 6, atau 8 jam.")
    upah_lembur= lembur if lembur >=1 <=3 else lembur *25000

    if lembur==4:
        upah_lembur=100000
    elif lembur==6:
        upah_lembur=200000
    elif lembur==8:
        upah_lembur=300000
    else:
        upah_lembur=0
    shift=input("apakah bekerja shift malam?(ya/tidak:").lower()
    if shift=="ya":
        upah_shift=50000
    else:
        upah_shift=0
    if lembur>0:
        lembur+=1
    else:
        print("tidak ada lembur")
    gaji_harian=gaji_pokok+upah_lembur+upah_shift
    total_gaji+=gaji_harian

    print(f"gaji hari ke-{hari}: Rp{gaji_harian:,}".replace(",","."))
print("\n======TOTAL GAJI ======")
print(f"total gaji:Rp {total_gaji:,}".replace(",","."))
print(f"total hari mengambil lembur:",lembur, ("hari"))