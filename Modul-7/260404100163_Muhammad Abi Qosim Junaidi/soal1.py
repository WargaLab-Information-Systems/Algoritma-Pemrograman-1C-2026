# Membuat dictionary kosong
menu = {}

while True:
    print("= MENU LIST =")
    print("1. Tambah Tugas")
    print("2. Tampilkan Tugas")
    print("3. Tandai Tugas Selesai")
    print("4. Hapus Tugas")
    print("5. Jumlah Tugas")
    print("6. Keluar")

    pilihan = input("Pilih menu (1-6): ")

    # Menambah tugas
    if pilihan == "1":
        tugas = input("Masukkan nama tugas: ")
        menu[tugas] = "Belum Selesai"
        print("Tugas berhasil ditambahkan!")

    # Menampilkan semua tugas
    elif pilihan == "2":
        if len(menu) == 0:
            print("Belum ada tugas.")
        else:
            print("Daftar Tugas:")
            for tugas, status in menu.items():
                print(tugas, ":", status)

    # Menandai tugas selesai
    elif pilihan == "3":
        tugas = input("Masukkan nama tugas: ")
        if tugas in menu:
            menu[tugas] = "Selesai"
            print("Tugas berhasil diselesaikan!")
        else:
            print("Tugas tidak ditemukan.")

    # Menghapus tugas
    elif pilihan == "4":
        tugas = input("Masukkan nama tugas: ")
        if tugas in menu:
            del menu[tugas]
            print("Tugas berhasil dihapus!")
        else:
            print("Tugas tidak ditemukan.")

    # Menghitung jumlah tugas
    elif pilihan == "5":
        selesai = 0
        belum = 0

        for status in menu.values():
            if status == "Selesai":
                selesai += 1
            else:
                belum += 1

        print("Jumlah tugas selesai:", selesai)
        print("Jumlah tugas belum selesai:", belum)

    # Keluar dari program
    elif pilihan == "6":
        print("Program selesai. Terima kasih!")
        break

    else:
        print("Pilihan tidak tersedia. Silakan coba lagi.")
