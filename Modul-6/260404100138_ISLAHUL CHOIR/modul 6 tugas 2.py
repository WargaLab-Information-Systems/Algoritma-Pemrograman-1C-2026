
asisten = []

while True:
    nama = input("Masukkan nama asisten (cukup untuk berhenti): ")

    if nama.lower() == "cukup":
        break

    asisten.append(nama)


asisten = tuple(asisten)


tambahan = input("Masukkan asisten tambahan: ")


asisten_baru = list(asisten)
asisten_baru.append(tambahan)


asisten_baru = tuple(asisten_baru)


hari = []

while True:
    nama_hari = input("Masukkan hari (cukup untuk berhenti): ")

    if nama_hari.lower() == "cukup":
        break

    hari.append(nama_hari)


hari = tuple(hari)


pengecualian = input("Nama asisten yang dikecualikan: ")
hari_libur = input("Hari pengecualian: ")


print("Jadwal Shift:")

for nama in asisten_baru:
    for h in hari:
        if nama == pengecualian and h == hari_libur:
            continue

        print(nama, "-", h)