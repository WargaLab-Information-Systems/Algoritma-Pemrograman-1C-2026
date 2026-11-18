tugas = {}

while True:
    print("\n=== TO-DO LIST ===")
    print("1. Tambah tugas")
    print("2. Tampilkan semua tugas")
    print("3. Tandai tugas selesai")
    print("4. Hapus tugas")
    print("5. Jumlah tugas selesai dan belum")
    print("6. Keluar")
    pilihan = input("Pilih menu (1-6) : ")

    if pilihan == "1":
        nama = input("Nama tugas : ")
        if nama in tugas:
            print("Tugas", nama, "sudah ada")
        else:
            tugas[nama] = "Belum selesai"
            print("Tugas", nama, "berhasil ditambahkan")

    elif pilihan == "2":
        if len(tugas) == 0:
            print("Belum ada tugas")
        else:
            nomor = 1
            for nama, status in tugas.items():
                print(str(nomor) + ".", nama, "-", status)
                nomor += 1

    elif pilihan == "3":
        nama = input("Nama tugas yang selesai : ")
        try:
            if tugas[nama] == "Selesai":
                print("Tugas", nama, "sudah berstatus selesai")
            else:
                tugas[nama] = "Selesai"
                print("Tugas", nama, "ditandai selesai")
        except KeyError:
            print("Tugas", nama, "tidak ditemukan")

    elif pilihan == "4":
        nama = input("Nama tugas yang dihapus : ")
        try:
            del tugas[nama]
            print("Tugas", nama, "berhasil dihapus")
        except KeyError:
            print("Tugas", nama, "tidak ditemukan")

    elif pilihan == "5":
        selesai = list(tugas.values()).count("Selesai")
        belum = len(tugas) - selesai
        print("Tugas selesai       :", selesai)
        print("Tugas belum selesai :", belum)

    elif pilihan == "6":
        print("Program selesai")
        break

    else:
        print("Menu tidak tersedia")
