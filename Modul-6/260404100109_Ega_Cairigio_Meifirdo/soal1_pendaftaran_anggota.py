daftar_nama = []

while True:
    nama = input("Nama calon anggota: ")
    if nama == "selesai":
        break
    daftar_nama.append(nama)

print("\n=== Hasil Pemeriksaan Nama ===")
for nama in daftar_nama:
    if nama == "admin" or len(nama) < 4:
        print(f"Nama '{nama}' tidak valid.")
    else:
        print(f"Nama '{nama}' valid.")

while True:
    penyusup = input("\nNama yang dicurigai sebagai penyusup: ")

    try:
        daftar_nama.remove(penyusup)
        print(f"Nama '{penyusup}' berhasil dihapus dari sistem.")
    except ValueError:
        print(f"Nama '{penyusup}' tidak ada di dalam pendaftaran.")

    pilihan = input("Apakah ingin memeriksa penyusup lagi? (ya/tidak): ")

    if pilihan == "tidak":
        break

print("\nDaftar anggota setelah pemeriksaan:", daftar_nama)
