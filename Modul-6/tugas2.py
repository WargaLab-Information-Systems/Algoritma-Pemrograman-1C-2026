
asisten_awal = []
while True:
    nama = input("Masukkan nama asisten awal : ")
    if nama == "cukup":
        break
    else:
        asisten_awal.append(nama)
asisten_awal = tuple(asisten_awal)

asisten_baru = input("Masukkan nama asisten tambahan: ")
asisten_akhir = asisten_awal + (asisten_baru,)

hari_tugas = []

while True:
    hari = input("Masukkan hari tugas: ")
    if hari == "cukup":
        break
    else:
        hari_tugas.append(hari)

hari_tugas = tuple(hari_tugas)
nama_pengecualian = input("Masukkan nama asisten pengecualian: ")
hari_pengecualian = input("Masukkan hari pengecualian: ")

print("Daftar jadwal shift:")

for nama in asisten_akhir:
    for hari in hari_tugas:
        if nama == nama_pengecualian and hari == hari_pengecualian:
            continue

        print(nama, "-", hari)
