asisten = []

while True:
    nama = input("Masukkan nama asisten (ketik cukup untuk berhenti): ")

    if nama == "cukup":
        break
    else:
        asisten.append(nama)

asisten = tuple(asisten)

tambahan = input("\nMasukkan nama asisten tambahan: ")

asisten_baru = asisten + (tambahan,)

hari = []

while True:
    nama_hari = input("Masukkan hari tugas (ketik cukup untuk berhenti): ")

    if nama_hari == "cukup":
        break
    else:
        hari.append(nama_hari)

hari = tuple(hari)

pengecualian = input("\nMasukkan nama asisten yang dikecualikan: ")
hari_libur = input("Masukkan hari pengecualian: ")

print("\nJadwal Shift Asisten Laboratorium:")

for nama in asisten_baru:
    for nama_hari in hari:
        if nama == pengecualian and nama_hari == hari_libur:
            continue

        print(nama, "-", nama_hari)