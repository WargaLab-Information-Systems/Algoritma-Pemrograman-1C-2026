playlist = {}

while True:
    print("\n===== MENU PLAYLIST MUSIK =====")
    print("1. Buat Playlist")
    print("2. Tambah Lagu")
    print("3. Tampilkan Semua Playlist")
    print("4. Cari Lagu")
    print("5. Hapus Lagu")
    print("6. Hapus Playlist")
    print("7. Keluar")

    pilihan = input("Pilih menu (1-7): ")

    if pilihan == "1":
        nama = input("Masukkan nama playlist: ")

        if nama not in playlist:
            playlist[nama] = {}
            print("Playlist berhasil dibuat!")
        else:
            print("Playlist sudah ada.")

    elif pilihan == "2":
        nama = input("Masukkan nama playlist: ")

        if nama in playlist:
            judul = input("Masukkan judul lagu: ")
            penyanyi = input("Masukkan nama penyanyi: ")

            playlist[nama][judul] = penyanyi

            print("Lagu berhasil ditambahkan!")
        else:
            print("Playlist tidak ditemukan.")

    elif pilihan == "3":
        if len(playlist) == 0:
            print("Belum ada playlist.")
        else:
            for nama in playlist:
                print("\nPlaylist:", nama)

                if len(playlist[nama]) == 0:
                    print("Belum ada lagu.")
                else:
                    for judul, penyanyi in playlist[nama].items():
                        print(judul, "-", penyanyi)

    elif pilihan == "4":
        cari = input("Masukkan judul lagu yang dicari: ")
        ditemukan = False

        for nama in playlist:
            if cari in playlist[nama]:
                print("Lagu ditemukan!")
                print("Playlist:", nama)
                print("Judul:", cari)
                print("Penyanyi:", playlist[nama][cari])
                ditemukan = True

        if ditemukan == False:
            print("Lagu tidak ditemukan.")

    elif pilihan == "5":
        nama = input("Masukkan nama playlist: ")

        if nama in playlist:
            judul = input("Masukkan judul lagu yang ingin dihapus: ")

            if judul in playlist[nama]:
                del playlist[nama][judul]
                print("Lagu berhasil dihapus!")
            else:
                print("Lagu tidak ditemukan.")
        else:
            print("Playlist tidak ditemukan.")

    elif pilihan == "6":
        nama = input("Masukkan nama playlist yang ingin dihapus: ")

        if nama in playlist:
            del playlist[nama]
            print("Playlist berhasil dihapus!")
        else:
            print("Playlist tidak ditemukan.")

    elif pilihan == "7":
        print("Program selesai. Terima kasih!")
        break

    else:
        print("Pilihan tidak tersedia.")