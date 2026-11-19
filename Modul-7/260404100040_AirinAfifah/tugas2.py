playlist = {}

while True:
    print("\nPROGRAM PLAYLIST MUSIK")
    print("1. buat playlist")
    print("2. tambah lagu ke playlist")
    print("3. tampilkan semua playlist")
    print("4. cari lagu")
    print("5. hapus lagu dari playlist")
    print("6. hapus playlist")
    print("7. keluar")

    pilihan = input("pilih menu (1-7): ")

    if pilihan == "1":
        nama_playlist = input("nama playlist: ")

        if nama_playlist in playlist:
            print("playlist sudah ada!")
        else:
            playlist[nama_playlist] = {}
            print("playlist berhasil dibuat!")

    elif pilihan == "2":
        nama_playlist = input("nama playlist: ")
        judul = input("judul lagu: ")
        penyanyi = input("nama penyanyi: ")

        try:
            playlist[nama_playlist][judul] = penyanyi
            print("lagu berhasil ditambahkan!")
        except KeyError:
            print("playlist tidak ditemukan!")

    elif pilihan == "3":
        if len(playlist) == 0:
            print("belum ada playlist.")
        else:
            for nama_playlist, lagu in playlist.items():
                print("\nplaylist:", nama_playlist)

                if len(lagu) == 0:
                    print("belum ada lagu.")
                else:
                    for judul, penyanyi in lagu.items():
                        print(judul, "-", penyanyi)

    elif pilihan == "4":
        cari = input("judul lagu yang dicari: ")
        ditemukan = False

        for nama_playlist, lagu in playlist.items():
            try:
                penyanyi = lagu[cari]
                print("lagu ditemukan!")
                print("judul lagu:", cari)
                print("penyanyi:", penyanyi)
                print("playlist:", nama_playlist)
                ditemukan = True
            except KeyError:
                pass

        if ditemukan == False:
            print("lagu tidak ditemukan!")

    elif pilihan == "5":
        nama_playlist = input("nama playlist: ")
        judul = input("judul lagu yang ingin dihapus: ")

        try:
            del playlist[nama_playlist][judul]
            print("lagu berhasil dihapus!")
        except KeyError:
            print("playlist atau lagu tidak ditemukan!")

    elif pilihan == "6":
        nama_playlist = input("nama playlist yang ingin dihapus: ")

        try:
            del playlist[nama_playlist]
            print("playlist berhasil dihapus!")
        except KeyError:
            print("playlist tidak ditemukan!")

    elif pilihan == "7":
        print("program playlist musik selesai.")
        break

    else:
        print("pilihan tidak valid!")