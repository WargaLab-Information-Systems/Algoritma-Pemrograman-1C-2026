tugas = {}

while True:
    print("\n=== TO-DO LIST ===")
    print("1. Tambah Tugas")
    print("2. Tampilkan Tugas")
    print("3. Tandai Selesai")
    print("4. Hapus Tugas")
    print("5. Jumlah Tugas")
    print("6. Keluar")

    pilih = input("Pilih menu: ")

    if pilih == "1":
        nama = input("Nama tugas: ")
        tugas[nama] = False
        print("Tugas berhasil ditambahkan")

    elif pilih == "2":
        if not tugas:
            print("Belum ada tugas")
        else:
            for nama, status in tugas.items():
                print(nama, "-", "Selesai" if status else "Belum selesai")

    elif pilih == "3":
        nama = input("Nama tugas: ")
        if nama in tugas:
            tugas[nama] = True
            print("Tugas selesai")
        else:
            print("Tugas tidak ditemukan")

    elif pilih == "4":
        nama = input("Nama tugas: ")
        if nama in tugas:
            del tugas[nama]
            print("Tugas berhasil dihapus")
        else:
            print("Tugas tidak ditemukan")

    elif pilih == "5":
        selesai = sum(tugas.values())
        print("Sudah selesai:", selesai)
        print("Belum selesai:", len(tugas) - selesai)

    elif pilih == "6":
         print("Program selesai")
         break
    else:
        print("Pilihan tidak valid")