anggota = []

while True:
    nama = str(input("Masukkan nama-nama calon anggota: "))

    if nama == "selesai":
        break
    anggota.append(nama)

print("\nPemeriksaan daftar anggota:")
for nama in anggota:
    if nama == "admin" or len(nama) < 4:
        print(nama, ": Nama tidak valid")
    else:
        print(nama, ": Nama valid")

while True:
    penyusup = str(input("\nMasukkan nama yg dicurigai sbgai penyusup untuk dihapus: "))
    if penyusup in anggota:
        anggota.remove(penyusup)
        print("Nama penyusup tersebut sudah dihapus")
        break
    else:
        print("Nama penyusup tersebut tidak ditemukan, coba lihat lagi daftar anggota")

print("\nJadi, daftar anggota klub robotika:", anggota)