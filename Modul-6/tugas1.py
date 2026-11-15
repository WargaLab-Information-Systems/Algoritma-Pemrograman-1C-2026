daftar_nama = []

while True:
    nama = input("Masukkan nama calon anggota: ")
    if nama == "selesai":
        break
    else:
        daftar_nama.append(nama)

print("Pemeriksaan nama anggota:")
for nama in daftar_nama:
    if nama == "admin" or len(nama) < 4:
        print(nama, "tidak valid")
    else:
        print(nama, "valid")

nama_hapus = input("Masukkan nama penyusup yang ingin dihapus: ")
if nama_hapus in daftar_nama:
    daftar_nama.remove(nama_hapus)
    print("Nama", nama_hapus, "berhasil dihapus")
else:
    print("Nama", nama_hapus, "tidak ditemukan")

print("Daftar nama akhir:", daftar_nama)