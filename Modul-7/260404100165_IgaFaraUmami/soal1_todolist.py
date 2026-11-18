tugas = {}

while True:
    print("\n=== TO-DO LIST ===")
    print("1. Tambah Tugas")
    print("2. Tampilkan Tugas")
    print("3. Tandai Selesai")
    print("4. Hapus Tugas")
    print("5. Hitung Tugas")
    print("6. Keluar")

    pilih = input("Pilih menu: ")

    if pilih == "1":
        nama = input("Nama tugas: ")
        tugas[nama] = "Belum Selesai"
        print("Tugas ditambahkan.")

    elif pilih == "2":
        for nama, status in tugas.items():
            print(nama, "=", status)

        if len(tugas) == 0:
            print("Belum ada tugas.")

    elif pilih == "3":
        nama = input("Nama tugas: ")
        if nama in tugas:
            tugas[nama] = "Selesai"
            print("Tugas selesai.")
        else:
            print("Tugas tidak ditemukan.")

    elif pilih == "4":
        nama = input("Nama tugas: ")
        if nama in tugas:
            del tugas[nama]
            print("Tugas dihapus.")
        else:
            print("Tugas tidak ditemukan.")

    elif pilih == "5":
        selesai = 0
        belum = 0

        for status in tugas.values():
            if status == "Selesai":
                selesai += 1
            else:
                belum += 1

        print("Tugas selesai:", selesai)
        print("Tugas belum selesai:", belum)

    elif pilih == "6":
        print("Program selesai.")
        break

    else:
        print("Pilihan tidak tersedia.")