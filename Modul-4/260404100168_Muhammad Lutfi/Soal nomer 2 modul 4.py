gaji_pokok = 100_000
tambahan_malam = 50_000
total_gaji = 0


def hitung_lembur(jam):
    if jam == 0:
        return 0
    if 1 <= jam <= 3:
        return jam * 25_000
    if jam == 4:
        return 100_000
    if jam == 6:
        return 200_000
    if jam == 8:
        return 300_000
    return None


for hari in range(1, 8):
    print(f"\n--- hari ke-{hari} ---")
    gaji_harian = gaji_pokok

    while True:
        jam = int(input("jumlah jam lembur: "))
        if jam > 8:
            print("jumlah lembur melebihi batas, upah lembur tidak dihitung")
            upah = 0
            break
        upah = hitung_lembur(jam)
        if upah is not None:
            break
        print("jam lembur tidak sesuai ketentuan, masukkan ulang")
    gaji_harian += upah

    while True:
        malam = input("shift malam? (y/n): ").strip().lower()
        if malam in ("y", "n"):
            break
        print("masukkan 'y' untuk ya atau 'n'.")

    if malam == "y":
        gaji_harian += tambahan_malam

    print(f"gaji hari ke-{hari}: Rp {gaji_harian:,}".replace(",", "."))
    total_gaji += gaji_harian

print(f"\nTotal gaji selama 7 hari: Rp {total_gaji:,}".replace(",", "."))