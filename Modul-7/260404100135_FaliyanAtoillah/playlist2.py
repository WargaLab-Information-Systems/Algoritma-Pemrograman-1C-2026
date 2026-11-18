playlist = {}

while True:
    print("\n===== DAFTAR PLAYLIST MUSIK =====")
    print("1. Membuat Playlist")
    print("2. Tambah Lagu ke Playlist")
    print("3. Lihat Semua Playlist")
    print("4. Mencari Lagu")
    print("5. Menghapus Lagu dari Playlist")
    print("6. Menghapus Playlist")
    print("7. Out")

    pilihan = input("Pilih menu (1-7): ")

    if pilihan == "1":
        nama_playlist = input("Masukkan nama playlist: ")

        if nama_playlist in playlist:
            print("Playlist sudah ada!")
        else:
            playlist[nama_playlist] = {}
            print("Playlist berhasil dibuat!")

    elif pilihan == "2":
        nama_playlist = input("Masukkan nama playlist: ")

        if nama_playlist in playlist:
            judul_lagu = input("Masukkan judul lagu: ")
            penyanyi = input("Masukkan nama penyanyi: ")

            if judul_lagu in playlist[nama_playlist]:
                print("Lagu sudah ada di playlist!")
            else:
                playlist[nama_playlist][judul_lagu] = penyanyi
                print("Lagu berhasil ditambahkan!")
        else:
            print("Playlist tidak ditemukan!")

    elif pilihan == "3":
        if not playlist:
            print("Belum ada playlist.")
        else:
            for nama_playlist, daftar_lagu in playlist.items():
                print(f"\nPlaylist: {nama_playlist}")

                if not daftar_lagu:
                    print("  Belum ada lagu.")
                else:
                    for judul_lagu, penyanyi in daftar_lagu.items():
                        print(f"  - {judul_lagu} : {penyanyi}")

    elif pilihan == "4":
        cari_lagu = input("Masukkan judul lagu yang dicari: ")
        ditemukan = False

        for nama_playlist, daftar_lagu in playlist.items():
            if cari_lagu in daftar_lagu:
                print("Lagu ditemukan!")
                print("Playlist:", nama_playlist)
                print("Judul lagu:", cari_lagu)
                print("Penyanyi:", daftar_lagu[cari_lagu])
                ditemukan = True

        if not ditemukan:
            print("Lagu tidak ada!")

    elif pilihan == "5":
        nama_playlist = input("Masukkan nama playlist: ")

        if nama_playlist in playlist:
            judul_lagu = input("Input lagu yang ingin dihapus: ")

            if judul_lagu in playlist[nama_playlist]:
                del playlist[nama_playlist][judul_lagu]
                print("Lagu berhasil dihapus!")
            else:
                print("Lagu tidak ada di playlist ini!")
        else:
            print("Playlist tidak ada!")

    elif pilihan == "6":
        nama_playlist = input("Masukkan nama playlist yang ingin dihapus: ")

        if nama_playlist in playlist:
            del playlist[nama_playlist]
            print("Playlist dihapus!")
        else:
            print("Playlist tidak ada!")

    if pilihan == "7":
        print("Terima kasih, program selesai!")
        break
