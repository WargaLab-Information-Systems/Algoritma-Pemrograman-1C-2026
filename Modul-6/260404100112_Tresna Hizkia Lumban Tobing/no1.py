anggota = []

while True:
    nama = input("Masukkan nama anggota (selesai untuk berhenti): ")

    if nama == "selesai":
        break

    anggota.append(nama)

print("\nDaftar anggota:")
print(anggota)

for nama in anggota:
    if nama == "admin" or len(nama) < 4:
        print(nama, "tidak valid")
    else:
        print(nama, "valid")

penyusup = input("\nMasukkan nama penyusup yang ingin dihapus: ")

try:
    anggota.remove(penyusup)
    print("Nama berhasil dihapus.")
except ValueError:
    print("Nama tidak ditemukan dalam pendaftaran.")

print("\nDaftar anggota akhir:")
print(anggota)