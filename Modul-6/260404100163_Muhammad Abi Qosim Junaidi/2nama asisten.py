# Memasukkan nama asisten awal
asisten = []

while True:
    nama = input("Masukkan nama asisten (ketik cukup untuk berhenti): ")

    if nama == "cukup":
        break

    asisten.append(nama)

# Mengunci data asisten awal menjadi tuple
asisten = tuple(asisten)

# Memasukkan satu asisten tambahan
tambahan = input("Masukkan nama asisten tambahan: ")

# Menggabungkan asisten awal dan tambahan
asisten_akhir = asisten + (tambahan,)

# Memasukkan nama-nama hari tugas
hari = []

while True:
    nama_hari = input("Masukkan hari tugas (ketik cukup untuk berhenti): ")

    if nama_hari == "cukup":
        break

    hari.append(nama_hari)

# Mengunci data hari menjadi tuple
hari = tuple(hari)

# Memasukkan pengecualian
pengecualian_asisten = input("Nama asisten yang dikecualikan: ")
pengecualian_hari = input("Hari yang dikecualikan: ")

# Membuat jadwal shift
print("Daftar Jadwal Shift:")

for nama in asisten_akhir:
    for nama_hari in hari:

        if nama == pengecualian_asisten and nama_hari == pengecualian_hari:
            continue

        print(nama, "-", nama_hari)
