daftar = []
while True:
    nama = input("Nama calon anggota: ")
    if nama == "selesai":
        break
    daftar.append(nama)

print("\nHasil pemeriksaan data:")
for nama in daftar:
    if nama == "admin" or len(nama) < 4:
        print("-", nama, "-> nama tidak valid")
    else:
        print("-", nama, "-> valid")

penyusup = input("\nNama yang dicurigai sebagai penyusup : ")
if penyusup in daftar:
    daftar.remove(penyusup)
    print("Nama", penyusup, "berhasil dihapus dari pendaftaran")
else:
    print("Nama", penyusup, "tidak ditemukan di dalam pendaftaran")

print("\nDaftar anggota akhir :", daftar)

