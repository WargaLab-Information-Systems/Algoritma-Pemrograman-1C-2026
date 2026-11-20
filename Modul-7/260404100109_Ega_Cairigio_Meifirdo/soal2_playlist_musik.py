playlist = {}

while True:
    print("\n=== MENU PENGELOLA PLAYLIST ===")
    print("1. Buat playlist")
    print("2. Tambah lagu ke playlist")
    print("3. Tampilkan semua playlist")
    print("4. Cari lagu")
    print("5. Hapus lagu dari playlist")
    print("6. Hapus playlist")
    print("7. Keluar")
    pilihan = input("Pilih menu (1-7): ").strip()

    if pilihan == "1":
        nama_pl = input("Nama playlist baru: ").strip()
        if nama_pl == "":
            print("Nama playlist tidak boleh kosong.")
        elif nama_pl in playlist:
            print(f"Playlist '{nama_pl}' sudah ada.")
        else:
            playlist[nama_pl] = {}
            print(f"Playlist '{nama_pl}' berhasil dibuat.")

    elif pilihan == "2":
        nama_pl = input("Nama playlist tujuan: ").strip()
        try:
            lagu_pl = playlist[nama_pl]
        except KeyError:
            print(f"Playlist '{nama_pl}' tidak ditemukan.")
        else:
            judul = input("Judul lagu: ").strip()
            penyanyi = input("Nama penyanyi: ").strip()
            if judul == "" or penyanyi == "":
                print("Judul dan penyanyi tidak boleh kosong.")
            elif judul in lagu_pl:
                print(f"Lagu '{judul}' sudah ada.")
            else:
                lagu_pl[judul] = penyanyi
                print(f"Lagu '{judul}' ditambahkan.")

    elif pilihan == "3":
        if len(playlist) == 0:
            print("Belum ada playlist.")
        else:
            for nama_pl, lagu_pl in playlist.items():
                print(f"\nPlaylist: {nama_pl}")
                if len(lagu_pl) == 0:
                    print("  (belum ada lagu)")
                else:
                    for judul, penyanyi in lagu_pl.items():
                        print(f"  - {judul} - {penyanyi}")

    elif pilihan == "4":
        cari = input("Judul lagu yang dicari: ").strip()
        if cari == "":
            print("Judul lagu yang dicari tidak boleh kosong.")
        else:
            ditemukan = False
            for nama, lagu in playlist.items():
                for judul, penyanyi in lagu.items():
                    if cari.lower() in judul.lower():
                        print(f"{judul} - {penyanyi} [{nama}]")
                        ditemukan = True
            if not ditemukan:
                print(f"Lagu '{cari}' tidak ditemukan.")

    elif pilihan == "5":
        nama_pl = input("Nama playlist: ").strip()
        try:
            lagu_pl = playlist[nama_pl]
        except KeyError:
            print(f"Playlist '{nama_pl}' tidak ditemukan.")
        else:
            judul = input("Judul lagu yang dihapus: ").strip()
            try:
                del lagu_pl[judul]
                print(f"Lagu '{judul}' dihapus.")
            except KeyError:
                print(f"Lagu '{judul}' tidak ada.")

    elif pilihan == "6":
        nama_pl = input("Playlist yang akan dihapus: ").strip()
        try:
            del playlist[nama_pl]
            print(f"Playlist '{nama_pl}' berhasil dihapus.")
        except KeyError:
            print(f"Playlist '{nama_pl}' tidak ditemukan.")

    elif pilihan == "7":
        print("Program selesai.")
        break

    else:
        print("Pilihan tidak valid, masukkan angka 1 sampai 7.")
