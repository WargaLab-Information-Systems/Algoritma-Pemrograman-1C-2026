asisten = []

while True:
    nama = input("nama asisten (ketik cukup untuk berhenti): ")

    if nama.lower() == "cukup":
        break

    asisten.append(nama)

asisten_awal = tuple(asisten)

tambahan = input("\nnama asisten tambahan: ")

asisten_akhir = asisten_awal + (tambahan,)

hari = []

while True:
    nama_hari = input("hari tugas (ketik cukup untuk berhenti): ")

    if nama_hari.lower() == "cukup":
        break

    hari.append(nama_hari)

hari_tugas = tuple(hari)

pengecualian_asisten = input("\nnama asisten yang dikecualikan: ")
pengecualian_hari = input("hari yang dikecualikan: ")

print("\njadwal shift asisten:")

for nama in asisten_akhir:
    for hari in hari_tugas:
        if nama == pengecualian_asisten and hari == pengecualian_hari:
            continue

        print(nama, "-", hari)