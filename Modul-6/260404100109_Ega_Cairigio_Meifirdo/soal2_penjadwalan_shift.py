asisten_list = []

while True:
    nama = input("Asisten awal: ")
    if nama == "cukup":
        break
    asisten_list.append(nama)
asisten_awal = tuple(asisten_list)

tambahan = input("Asisten tambahan: ")
asisten_akhir = asisten_awal + (tambahan,)

hari_list = []
while True:
    hari = input("Hari tugas: ")
    if hari == "cukup":
        break
    hari_list.append(hari)
hari_tugas = tuple(hari_list)

asisten_kecuali = input("Asisten yang dikecualikan: ")
hari_kecuali = input("Hari pengecualian: ")

print("\n=== Jadwal Shift Asisten ===")
for asisten in asisten_akhir:
    for hari in hari_tugas:
        asisten_sama = asisten == asisten_kecuali
        hari_sama = hari == hari_kecuali
        if asisten_sama and hari_sama:
            continue
        print(f"Shift: {asisten} - {hari}")
