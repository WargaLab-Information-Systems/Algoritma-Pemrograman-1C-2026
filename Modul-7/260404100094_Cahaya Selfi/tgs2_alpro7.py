# Soal 2 - Playlist Musik (dictionary di dalam dictionary)
playlist = {}

while True:
    print("\n--- MENU PLAYLIST ---")
    print("1. Buat playlist")
    print("2. Tambah lagu")
    print("3. Tampilkan semua playlist")
    print("4. Cari lagu")
    print("5. Hapus lagu")
    print("6. Hapus playlist")
    print("7. Keluar")
    pilih = input("Pilih menu: ")

    if pilih == "1":
        nama = input("Nama playlist: ")
        if nama in playlist:
            print("Playlist sudah ada.")
        else:
            playlist[nama] = {}
            print("Playlist dibuat!")

    elif pilih == "2":
        nama = input("Nama playlist: ")
        if nama in playlist:
            judul = input("Judul lagu: ")
            penyanyi = input("Penyanyi: ")
            playlist[nama][judul] = penyanyi
            print("Lagu ditambahkan!")
        else:
            print("Playlist tidak ditemukan.")

    elif pilih == "3":
        if len(playlist) == 0:
            print("Belum ada playlist.")
        else:
            for nama in playlist:
                print("Playlist:", nama)
                if len(playlist[nama]) == 0:
                    print("  (belum ada lagu)")
                else:
                    for judul in playlist[nama]:
                        print("  -", judul, "oleh", playlist[nama][judul])

    elif pilih == "4":
        cari = input("Judul lagu yang dicari: ")
        ketemu = False
        for nama in playlist:
            if cari in playlist[nama]:
                print("Ditemukan di playlist", nama, "- penyanyi:", playlist[nama][cari])
                ketemu = True
        if not ketemu:
            print("Lagu tidak ditemukan.")

    elif pilih == "5":
        nama = input("Nama playlist: ")
        if nama in playlist:
            judul = input("Judul lagu yang dihapus: ")
            if judul in playlist[nama]:
                del playlist[nama][judul]
                print("Lagu dihapus!")
            else:
                print("Lagu tidak ditemukan.")
        else:
            print("Playlist tidak ditemukan.")

    elif pilih == "6":
        nama = input("Playlist yang dihapus: ")
        if nama in playlist:
            del playlist[nama]
            print("Playlist dihapus!")
        else:
            print("Playlist tidak ditemukan.")

    elif pilih == "7":
        print("Sampai jumpa!")
        break

    else:
        print("Menu tidak valid.")