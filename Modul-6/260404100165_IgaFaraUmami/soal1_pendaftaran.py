anggota = []

while True:
    nama = input("Masukkan nama (selesai untuk berhenti): ")

    if nama == "selesai":
        break

    anggota.append(nama)

print("\nHasil pemeriksaan:")

for nama in anggota:
    if nama == "admin" or len(nama) < 4:
        print(nama, "tidak valid")
    else:
        print(nama, "valid")

hapus = input("\nMasukkan nama yang ingin dihapus: ")

if hapus in anggota:
    anggota.remove(hapus)
    print("Nama berhasil dihapus")
else:
    print("Nama tidak ditemukan")

print("\nDaftar anggota:", anggota)