anggota = []

while True:
    nama = input("nama calon anggota (ketik selesai untuk berhenti): ")

    if nama.lower() == "selesai":
        break

    anggota.append(nama)

print("\ndaftar calon anggota:")
for nama in anggota:
    if nama.lower() == "admin" or len(nama) < 4:
        print(nama, "- nama tidak valid")
    else:
        print(nama, "- nama valid")

hapus = input("\nnama yang ingin dihapus: ")

if hapus in anggota:
    anggota.remove(hapus)
    print("nama", hapus, "berhasil dihapus.")
else:
    print("nama", hapus, "tidak ditemukan.")

print("\ndaftar anggota setelah penghapusan:", anggota)