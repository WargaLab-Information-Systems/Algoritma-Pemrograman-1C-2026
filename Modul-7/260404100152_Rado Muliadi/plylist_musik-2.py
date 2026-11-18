playlist = {}

while True:
    print("\n=== PENGELOLA PLAYLIST MUSIK ===")
    print("1. Buat playlist")
    print("2. Tambah lagu ke playlist")
    print("3. Tampilkan semua playlist")
    print("4. Cari lagu")
    print("5. Hapus lagu dari playlist")
    print("6. Hapus playlist")
    print("7. Keluar")
    pilihan = input("Pilih menu (1-7) : ")

    if pilihan == "1":
        nama_pl = input("Nama playlist : ")
        if nama_pl in playlist:
            print("Playlist", nama_pl, "sudah ada")
        else:
            playlist[nama_pl] = {}
            print("Playlist", nama_pl, "berhasil dibuat")

    elif pilihan == "2":
        nama_pl = input("Nama playlist : ")
        try:
            lagu = playlist[nama_pl]
            judul = input("Judul lagu : ")
            penyanyi = input("Penyanyi : ")
            lagu[judul] = penyanyi
            print("Lagu", judul, "ditambahkan ke", nama_pl)
        except KeyError:
            print("Playlist", nama_pl, "tidak ditemukan")

    elif pilihan == "3":
        if len(playlist) == 0:
            print("Belum ada playlist")
        else:
            for nama_pl, lagu in playlist.items():
                print("Playlist:", nama_pl)
                if len(lagu) == 0:
                    print("   (kosong)")
                else:
                    for judul, penyanyi in lagu.items():
                        print("   -", judul, "oleh", penyanyi)

    elif pilihan == "4":
        judul = input("Judul lagu yang dicari : ")
        ditemukan = False
        for nama_pl, lagu in playlist.items():
            if judul in lagu:
                print("Ditemukan di", nama_pl, "->", judul, "oleh", lagu[judul])
                ditemukan = True
        if not ditemukan:
            print("Lagu", judul, "tidak ditemukan")

    elif pilihan == "5":
        nama_pl = input("Nama playlist : ")
        try:
            lagu = playlist[nama_pl]
            judul = input("Judul lagu yang dihapus : ")
            try:
                del lagu[judul]
                print("Lagu", judul, "dihapus dari", nama_pl)
            except KeyError:
                print("Lagu", judul, "tidak ada di", nama_pl)
        except KeyError:
            print("Playlist", nama_pl, "tidak ditemukan")

    elif pilihan == "6":
        nama_pl = input("Nama playlist yang dihapus : ")
        try:
            del playlist[nama_pl]
            print("Playlist", nama_pl, "berhasil dihapus")
        except KeyError:
            print("Playlist", nama_pl, "tidak ditemukan")

    elif pilihan == "7":
        print("Program selesai")
        break

    else:
        print("Menu tidak tersedia")

