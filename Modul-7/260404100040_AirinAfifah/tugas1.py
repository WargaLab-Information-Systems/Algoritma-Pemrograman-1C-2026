tugas = {}

while True:
    print("\nPROGRAM TO-DO LIST")
    print("1. tambah tugas")
    print("2. tampilkan semua tugas")
    print("3. tandai tugas selesai")
    print("4. hapus tugas")
    print("5. jumlah tugas selesai dan belum selesai")
    print("6. keluar")

    pilihan = input("pilih menu (1-6): ")

    if pilihan == "1":
        nama = input("nama tugas: ")

        if nama in tugas:
            print("tugas sudah ada!")
        else:
            tugas[nama] = "belum selesai"
            print("tugas berhasil ditambahkan!")

    elif pilihan == "2":
        if len(tugas) == 0:
            print("belum ada tugas.")
        else:
            print("\ndaftar tugas:")
            for nama, status in tugas.items():
                print(nama, ":", status)

    elif pilihan == "3":
        nama = input("nama tugas yang selesai: ")
        try:
            tugas[nama]
            tugas[nama] = "selesai"
            print("tugas berhasil ditandai selesai!")
        except KeyError:
            print("tugas tidak ditemukan!")

    elif pilihan == "4":
        nama = input("nama tugas yang ingin dihapus: ")
        try:
            del tugas[nama]
            print("tugas berhasil dihapus!")
        except KeyError:
            print("tugas tidak ditemukan!")

    elif pilihan == "5":
        selesai = 0
        belum_selesai = 0

        for status in tugas.values():
            if status.lower() == "selesai":
                selesai += 1
            else:
                belum_selesai += 1

        print("jumlah tugas selesai:", selesai)
        print("jumlah tugas belum selesai:", belum_selesai)

    elif pilihan == "6":
        print("program to-do list selesai.")
        break

    else:
        print("pilihan tidak valid!")