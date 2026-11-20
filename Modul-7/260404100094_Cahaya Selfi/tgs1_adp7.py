# Soal 1 - To-Do List
tugas = {}

while True:
    print("\n--- MENU TO-DO LIST ---")
    print("1. Tambah tugas")
    print("2. Tampilkan semua tugas")
    print("3. Tandai tugas selesai")
    print("4. Hapus tugas")
    print("5. Jumlah tugas selesai & belum")
    print("6. Keluar")
    pilih = input("Pilih menu: ")

    if pilih == "1":
        nama = input("Nama tugas: ")
        tugas[nama] = "Belum selesai"
        print("Tugas ditambahkan!")

    elif pilih == "2":
        if len(tugas) == 0:
            print("Belum ada tugas.")
        else:
            for nama in tugas:
                print(nama, "-", tugas[nama])

    elif pilih == "3":
        nama = input("Tugas yang selesai: ")
        if nama in tugas:
            tugas[nama] = "Selesai"
            print("Tugas ditandai selesai!")
        else:
            print("Tugas tidak ditemukan.")

    elif pilih == "4":
        nama = input("Tugas yang dihapus: ")
        if nama in tugas:
            del tugas[nama]
            print("Tugas dihapus!")
        else:
            print("Tugas tidak ditemukan.")

    elif pilih == "5":
        selesai = 0
        belum = 0
        for nama in tugas:
            if tugas[nama] == "Selesai":
                selesai += 1
            else:
                belum += 1
        print("Tugas selesai:", selesai)
        print("Tugas belum selesai:", belum)

    elif pilih == "6":
        print("Sampai jumpa!")
        break

    else:
        print("Menu tidak valid.")