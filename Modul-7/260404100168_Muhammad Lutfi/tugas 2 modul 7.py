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
        if nama not in playlist:
            playlist[nama] = {}
            print("Playlist berhasil dibuat")
        else:
            print("Playlist sudah ada")

    elif pilih == "2":
        nama = input("Nama playlist: ")
        if nama in playlist:
            judul = input("Judul lagu: ")
            penyanyi = input("Nama penyanyi: ")
            playlist[nama][judul] = penyanyi
            print("Lagu berhasil ditambahkan")
        else:
            print("Playlist tidak ditemukan")

    elif pilih == "3":
        if not playlist:
            print("Belum ada playlist")
        else:
            for nama, lagu in playlist.items():
                print("\nPlaylist:", nama)
                for judul, penyanyi in lagu.items():
                    print(judul, "-", penyanyi)

    elif pilih == "4":
        judul = input("Judul lagu: ")
        ditemukan = False

        for nama, lagu in playlist.items():
            if judul in lagu:
                print("Ditemukan di:", nama)
                print("Penyanyi:", lagu[judul])
                ditemukan = True

        if not ditemukan:
            print("Lagu tidak ditemukan")

    elif pilih == "5":
        nama = input("Nama playlist: ")
        if nama in playlist:
            judul = input("Judul lagu: ")
            if judul in playlist[nama]:
                del playlist[nama][judul]
                print("Lagu berhasil dihapus")
            else:
                print("Lagu tidak ditemukan")
        else:
            print("Playlist tidak ditemukan")

    elif pilih == "6":
        nama = input("Nama playlist: ")
        if nama in playlist:
            del playlist[nama]
            print("Playlist berhasil dihapus")
        else:
            print("Playlist tidak ditemukan")

    elif pilih == "7":
        print("Program selesai")
        break

    else:
        print("Pilihan tidak valid")