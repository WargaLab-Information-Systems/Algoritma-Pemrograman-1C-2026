anggota = []

while True:
    nama = input("Masukkan nama anggota ('selesai' untuk berhenti): ")

    if nama == "selesai":
        break
#isi data anggota ke list
    anggota.append(nama)

print("\nHasil pemeriksaan anggota:")
#periksa nama
for nama in anggota:
    if nama == "admin" or len(nama) < 4:
        print(nama, "Tidak Valid")
    else:
        print(nama, "Valid")

hapus = input("\nMasukkan nama penyusup yang ingin dihapus: ")

if hapus in anggota:
    anggota.remove(hapus)
    print("anggota berhasil dihapus")
else:
    print("anggota tidak ditemukan")

print("\nDaftar anggota akhir:")

for nama in anggota:
    print(nama)