todo_list = {}

while True:
    print("\n==DAFTAR TO-DO LIST==")
    print("1. Tambah Tugas")
    print("2. Lihat Semua Tugas")
    print("3. pilih Tugas Selesai")
    print("4. Delete Tugas")
    print("5. jumlah tugas akhir")
    print("6. Out")

    pilihan = input("Pilih diantaranya (1-6): ")

    if pilihan == "1":
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
    

    elif pilihan == "2":
        if not todo_list:
            print("Belum ada tugas.")
        else:
            print("\nDaftar Tugas:")
            for tugas, status in todo_list.items():
                print(f"- {tugas} : {status}")

    elif pilihan == "3":
        while True:
            nama_tugas = input("\nMasukkan nama tugas yang selesai: ").strip().upper()
            if nama_tugas == "":
                print("Nama tugas tidak boleh kosong.")
            else:
                break

        if nama_tugas in todo_list:
            todo_list[nama_tugas] = "Selesai"
            print("Tugas berhasil ditandai selesai!")
        else:
            print("Tugas tidak ada!")
    
    elif pilihan == "4":
        while True:
            nama_tugas = input("\nMasukkan nama tugas yang ingin dihapus: ").strip().upper()
            if nama_tugas == "":
                print("Nama tugas tidak boleh kosong.")
            else:
                break

        if nama_tugas in todo_list:
            del todo_list[nama_tugas]
            print("Tugas berhasil dihapus!")
        else:
            print("Tugas tidak ada!")

    elif pilihan == "5":
        selesai = 0
        belum_selesai = 0

        for status in todo_list.values():
            if status == "Selesai":
                selesai += 1
            else:
                belum_selesai += 1

        print("Jumlah tugas selesai:", selesai)
        print("Jumlah tugas belum selesai:", belum_selesai)

    if pilihan == "6":
        print("Terima kasih, program selesai.")
        break