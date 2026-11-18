
todo_list = {}

while True:
    print("\n=== MENU TO-DO LIST ===")
    print("1. Tambah Tugas")
    print("2. Tampilkan Semua Tugas")
    print("3. Tandai Tugas Selesai")
    print("4. Tandai Tugas Belum Selesai")
    print("5. Hapus Tugas")
    print("6. Statistik Tugas")
    print("7. Keluar")

    try:
        pilihan = int(input("Pilih menu: "))
    except ValueError:
        print("\nInput tidak valid, harus berupa angka sesuai pilihan.")
        continue
    
    if pilihan == 7:
        print("\nProgram selesai.")
        break

    elif pilihan == 1:
        while True:
            nama_tugas = input("\nMasukkan nama tugas: ").strip().upper()
            if nama_tugas == "":
                print("Nama tugas tidak boleh kosong.")
            else:
                break

        if nama_tugas in todo_list:
            print(f"Tugas {nama_tugas} sudah tersedia.")
        else:
            todo_list[nama_tugas] = "Belum Selesai"
            print(f"Tugas {nama_tugas} berhasil ditambahkan.")

    elif pilihan == 2:
        if not todo_list:
            print("\nBelum ada tugas.")
        else:
            print("\n=== DAFTAR TUGAS ===")
            for key, value in todo_list.items():
                print(f"- {key} | {value}")

    elif pilihan == 3:
        while True:
            nama_tugas = input("\nMasukkan nama tugas: ").strip().upper()
            if nama_tugas == "":
                print("Nama tidak boleh kosong.")
            else:
                break

        if nama_tugas in todo_list:
            todo_list[nama_tugas] = "Selesai"
            print(f"Tugas {nama_tugas} berhasil diubah menjadi Selesai.")
        else:
            print(f"Tugas {nama_tugas} tidak ditemukan.")

    elif pilihan == 4:
        while True:
            nama_tugas = input("\nMasukkan nama tugas: ").strip().upper()
            if nama_tugas == "":
                print("Nama tidak boleh kosong.")
            else:
                break

        if nama_tugas in todo_list:
            todo_list[nama_tugas] = "Belum Selesai"
            print(f"Tugas {nama_tugas} berhasil diubah menjadi Belum Selesai.")
        else:
            print(f"Tugas {nama_tugas} tidak ditemukan.")

    elif pilihan == 5:
        while True:
            nama_tugas = input("\nMasukkan nama tugas: ").strip().upper()
            if nama_tugas == "":
                print("Nama tidak boleh kosong.")
            else:
                break

        if nama_tugas in todo_list:
            del todo_list[nama_tugas]
            print(f"Tugas {nama_tugas} berhasil dihapus.")
        else:
            print(f"Tugas {nama_tugas} tidak ditemukan.")

    elif pilihan == 6:
        selesai = 0
        belum_selesai = 0

        for status in todo_list.values():
            if status == "Selesai":
                selesai += 1
            else:
                belum_selesai += 1

        print("\n=== STATISTIK TUGAS ===")
        print(f"Total semua tugas         : {len(todo_list)}")
        print(f"Jumlah tugas selesai      : {selesai}")
        print(f"Jumlah tugas belum selesai: {belum_selesai}")

    else:
        print("\nPilihan di luar rentang, ulangi.")