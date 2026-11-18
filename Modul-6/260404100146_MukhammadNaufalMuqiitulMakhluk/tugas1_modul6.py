daftar_nama = []

while True:
    nama = input("Masukkan nama anggota (ketik selesai untuk berhenti): ")

    if nama == "selesai":
        break
    else:
        daftar_nama.append(nama)

print("\nDaftar pemeriksaan nama anggota:")

for nama in daftar_nama:
    if nama == "admin" or len(nama) < 4:
        print(nama, "tidak valid")
    else:
        print(nama, "valid")

penyusup = input("\nMasukkan nama penyusup yang ingin dihapus: ")

if penyusup in daftar_nama:
    daftar_nama.remove(penyusup)
    print("Nama", penyusup, "berhasil dihapus")
else:
    print("Nama", penyusup, "tidak ditemukan dalam daftar")

print("\nDaftar anggota setelah diperbarui:")
print(daftar_nama)