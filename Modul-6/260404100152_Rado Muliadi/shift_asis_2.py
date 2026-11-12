asisten_awal = ()
while True:
    nama = input("Nama asisten awal : ")
    if nama == "cukup":
        break
    asisten_awal = asisten_awal + (nama,)

tambahan = input("Nama asisten tambahan : ")
asisten_akhir = asisten_awal + (tambahan,)

hari_tugas = ()
while True:
    hari = input("Hari tugas : ")
    if hari == "cukup":
        break
    hari_tugas = hari_tugas + (hari,)

nama_kecuali = input("Nama asisten pengecualian : ")
hari_kecuali = input("Hari pengecualian : ")

print("\nJadwal shift asisten laboratorium:")
for asisten in asisten_akhir:
    for hari in hari_tugas:
        if asisten == nama_kecuali and hari == hari_kecuali:
            continue
        print("Shift:", asisten, "-", hari)
