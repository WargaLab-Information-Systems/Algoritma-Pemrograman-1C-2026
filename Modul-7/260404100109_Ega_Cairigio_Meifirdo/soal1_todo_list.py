tugas = {}

while True:
    print("\n=== MENU TO-DO LIST ===")
    print("1. Tambah tugas")
    print("2. Tampilkan semua tugas")
    print("3. Tandai tugas selesai")
    print("4. Hapus tugas")
    print("5. Jumlah tugas selesai dan belum")
    print("6. Keluar")
    pilihan = input("Pilih menu (1-6): ").strip()

    if pilihan == "1":
        nama = input("Nama tugas: ").strip()
        if nama == "":
            print("Nama tugas tidak boleh kosong.")
        elif nama in tugas:
            print(f"Tugas '{nama}' sudah ada di daftar.")
        else:
            tugas[nama] = "Belum selesai"
            print(f"Tugas '{nama}' berhasil ditambahkan.")

    elif pilihan == "2":
        if len(tugas) == 0:
            print("Daftar tugas masih kosong.")
        else:
            print("\nDaftar Tugas:")
            nomor = 1
            for nama, status in tugas.items():
                print(f"{nomor}. {nama} - {status}")
                nomor += 1

    elif pilihan == "3":
        nama = input("Nama tugas yang sudah selesai: ").strip()
        try:
            if tugas[nama] == "Selesai":
                print(f"Tugas '{nama}' sudah selesai.")
            else:
                tugas[nama] = "Selesai"
                print(f"Tugas '{nama}' ditandai selesai.")
        except KeyError:
            print(f"Tugas '{nama}' tidak ditemukan.")

    elif pilihan == "4":
        nama = input("Nama tugas yang akan dihapus: ").strip()
        try:
            del tugas[nama]
            print(f"Tugas '{nama}' berhasil dihapus.")
        except KeyError:
            print(f"Tugas '{nama}' tidak ditemukan.")

    elif pilihan == "5":
        selesai = list(tugas.values()).count("Selesai")
        belum = len(tugas) - selesai
        print(f"Tugas selesai : {selesai}")
        print(f"Tugas belum   : {belum}")

    elif pilihan == "6":
        print("Program selesai.")
        break

    else:
        print("Pilihan tidak valid, masukkan angka 1 sampai 6.")
