playlist = {}

while True:
    print("\n=== PLAYLIST MUSIK ===")
    print("1. Buat Playlist")
    print("2. Tambah Lagu")
    print("3. Tampilkan Playlist")
    print("4. Cari Lagu")
    print("5. Hapus Lagu")
    print("6. Hapus Playlist")
    print("7. Keluar")

    pilih = input("Pilih menu: ")

    if pilih == "1":
        nama = input("Nama playlist: ")
        playlist[nama] = {}
        print("Playlist berhasil dibuat.")

    elif pilih == "2":
        nama = input("Nama playlist: ")

        if nama in playlist:
            judul = input("Judul lagu: ")
            penyanyi = input("Nama penyanyi: ")
            playlist[nama][judul] = penyanyi
            print("Lagu berhasil ditambahkan.")
        else:
            print("Playlist tidak ditemukan.")

    elif pilih == "3":
        for nama in playlist:
            print("\nPlaylist:", nama)

            for judul in playlist[nama]:
                print(judul, "-", playlist[nama][judul])

        if len(playlist) == 0:
            print("Belum ada playlist.")

    elif pilih == "4":
        judul = input("Cari judul lagu: ")
        ada = False

        for nama in playlist:
            if judul in playlist[nama]:
                print("Lagu:", judul)
                print("Penyanyi:", playlist[nama][judul])
                print("Playlist:", nama)
                ada = True

        if ada == False:
            print("Lagu tidak ditemukan.")

    elif pilih == "5":
        nama = input("Nama playlist: ")

        if nama in playlist:
            judul = input("Judul lagu: ")

            if judul in playlist[nama]:
                del playlist[nama][judul]
                print("Lagu berhasil dihapus.")
            else:
                print("Lagu tidak ditemukan.")
        else:
            print("Playlist tidak ditemukan.")

    elif pilih == "6":
        nama = input("Nama playlist: ")

        if nama in playlist:
            del playlist[nama]
            print("Playlist berhasil dihapus.")
        else:
            print("Playlist tidak ditemukan.")

    elif pilih == "7":
        print("Program selesai.")
        break

    else:
        print("Pilihan tidak valid.")