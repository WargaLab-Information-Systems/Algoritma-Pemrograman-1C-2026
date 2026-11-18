asisten = []

while True:
    nama = input("Masukkan nama asisten (cukup untuk berhenti): ")

    if nama.lower() == "cukup":
        break

    asisten.append(nama)

# Mengunci data awal
asisten = tuple(asisten)

# Menambahkan asisten baru
tambahan = input("Masukkan asisten tambahan: ")

# Menggabungkan data
asisten_baru = list(asisten)
asisten_baru.append(tambahan)

# Mengunci kembali data
asisten_baru = tuple(asisten_baru)

# Input hari
hari = []

while True:
    nama_hari = input("Masukkan hari (cukup untuk berhenti): ")

    if nama_hari.lower() == "cukup":
        break

    hari.append(nama_hari)

# Mengunci data hari
hari = tuple(hari)

# Input pengecualian
pengecualian = input("Nama asisten yang dikecualikan: ")
hari_libur = input("Hari pengecualian: ")

# Membuat jadwal
print("\nJadwal Shift:")

for nama in asisten_baru:
    for h in hari:
        if nama == pengecualian and h == hari_libur:
            continue

        print(nama, "-", h)