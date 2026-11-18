# Membuat list untuk menyimpan nama anggota
anggota = []

# Memasukkan nama anggota
while True:
    nama = input("Masukkan nama anggota (ketik selesai untuk berhenti): ")

    if nama == "selesai":
        break

    anggota.append(nama)

# Memeriksa nama anggota  
print("Hasil pemeriksaan nama:")

for nama in anggota:
    if nama == "admin" or len(nama) < 4:
        print(nama, "tidak valid")
    else:
        print(nama, "valid")

# Menghapus nama penyusup
hapus = input("Masukkan nama yang ingin dihapus: ")

if hapus in anggota:
    anggota.remove(hapus)
    print("Nama berhasil dihapus")
else:
    print("Nama tidak ditemukan")

# Menampilkan daftar anggota akhir
print("Daftar anggota setelah penghapusan:")
print(anggota)
