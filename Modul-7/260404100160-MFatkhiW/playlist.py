
playlist = {}

while True:
    print("\n=== MENU PLAYLIST MUSIK ===")
    print("1. Buat Playlist")
    print("2. Tambah Lagu")
    print("3. Tampilkan Semua Playlist")
    print("4. Cari Lagu")
    print("5. Hapus Lagu")
    print("6. Hapus Playlist")
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
            nama_playlist = input("\nMasukkan nama playlist: ").strip().title()
            if nama_playlist == "":
                print("Nama playlist tidak boleh kosong.")
            else:
                break

        if nama_playlist in playlist:
            print("Playlist sudah tersedia.")
        else:
            playlist[nama_playlist] = {}
            print(f"Playlist {nama_playlist} berhasil dibuat.")

    elif pilihan == 2:
        while True:
            nama_playlist = input("\nMasukkan nama playlist: ").strip().title()
            if nama_playlist == "":
                print("Nama playlist tidak boleh kosong.")
            else:
                break

        if nama_playlist not in playlist:
            print("Playlist tidak ditemukan.")
            continue

        while True:
            judul_lagu = input("Masukkan judul lagu: ").strip().title()
            if judul_lagu == "":
                print("Nama lagu tidak boleh kosong.")
            else:
                break

        while True:
            penyanyi = input("Masukkan nama penyanyi: ").strip().title()
            if penyanyi == "":
                print("Nama penyanyi tidak boleh kosong.")
            else:
                break

        if judul_lagu in playlist[nama_playlist]:
            print("Lagu sudah tersedia di playlist.")
        else:
            playlist[nama_playlist][judul_lagu] = penyanyi
            print(f"Lagu {judul_lagu} berhasil ditambahkan.")

    elif pilihan == 3:
        if not playlist:
            print("\nBelum ada playlist.")
        else:
            print("\n=== DAFTAR PLAYLIST ===")

            for nama, daftar_lagu in playlist.items():
                print(f"Playlist: {nama}")

                if not daftar_lagu:
                    print("  Belum ada lagu.")
                else:
                    for judul, penyanyi in daftar_lagu.items():
                        print(f"  - {judul} | {penyanyi}")

    elif pilihan == 4:
        if not playlist:
            print("\nBelum ada playlist.")
            continue

        while True:
            judul_lagu = input("\nMasukkan judul lagu: ").strip().title()
            if judul_lagu == "":
                print("Nama lagu tidak boleh kosong.")
            else:
                break
        ditemukan = False

        for nama, daftar_lagu in playlist.items():
            if judul_lagu in daftar_lagu:
                print(f"Lagu ditemukan!")
                print(f"Playlist: {nama}")
                print(f"Judul: {judul_lagu}")
                print(f"Penyanyi: {daftar_lagu[judul_lagu]}")
                ditemukan = True

        if not ditemukan:
            print("Lagu tidak ditemukan.")

    elif pilihan == 5:
        while True:
            nama_playlist = input("\nMasukkan nama playlist: ").strip().title()
            if nama_playlist == "":
                print("Nama playlist tidak boleh kosong.")
            else:
                break

        if nama_playlist not in playlist:
            print("Playlist tidak ditemukan.")
            continue

        while True:
            judul_lagu = input("Masukkan judul lagu: ").strip().title()
            if judul_lagu == "":
                print("Nama lagu tidak boleh kosong.")
            else:
                break

        if judul_lagu in playlist[nama_playlist]:
            del playlist[nama_playlist][judul_lagu]
            print(f"Lagu {judul_lagu} berhasil dihapus.")
        else:
            print("Lagu tidak ditemukan.")

    elif pilihan == 6:
        while True:
            nama_playlist = input("\nMasukkan nama playlist: ").strip().title()
            if nama_playlist == "":
                print("Nama playlist tidak boleh kosong.")
            else:
                break

        if nama_playlist in playlist:
            del playlist[nama_playlist]
            print(f"Playlist {nama_playlist} berhasil dihapus.")
        else:
            print("Playlist tidak ditemukan.")

    else:
        print("\nPilihan di luar rentang, ulangi.")