daftar_nama = []

while True:
    nama = input("Masukkan nama anggota (selesai untuk berhenti): ")

    if nama.lower() == "selesai":
        break

    daftar_nama.append(nama)

print("Hasil Pemeriksaan:")

for nama in daftar_nama:
    if nama.lower() == "admin" or len(nama) < 4:
        print(nama, "Tidak Valid")
    else:
        print(nama, "Valid")

hapus = input("Masukkan nama yang ingin dihapus: ")

if hapus in daftar_nama:
    daftar_nama.remove(hapus)
    print("Nama berhasil dihapus.")
else:
    print("Nama tidak ditemukan.")

print("Daftar Nama Akhir:", daftar_nama)