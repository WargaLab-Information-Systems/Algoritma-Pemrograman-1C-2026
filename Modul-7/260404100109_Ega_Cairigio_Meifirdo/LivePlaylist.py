playlist={}

while True:
    print('\n Menu Playlist Musik')
    print('1. Buat Playlist')
    print('2. Tambahkan Lagu ke Playlist')
    print('3. Tampilkan Semua Playlist')
    print('4. Cari Lagu')
    print('5. Hapus Lagu')
    print('6. Hapus Playlist')
    print('7. Keluar')
    pilihan = input('pilih menu angka: ')

    if pilihan == '1':
        nama_playlist = input('Nama playlist baru: ')
        if nama_playlist == '':
            print('Nama playlist tidak boleh kosong.')
        elif nama_playlist in playlist:
            print(f"Playlist '{nama_playlist}' sudah ada.")
        else:
            playlist[nama_playlist] = {}
            print(f"Playlist '{nama_playlist}' berhasil dibuat.")

    elif pilihan == '2':
        nama_playlist = input('Nama playlist tujuan: ')
        try:
            lagu_playlist = playlist[nama_playlist]
        except KeyError:
            print(f"Playlist '{nama_playlist}' tidak ditemukan.")
        else:
            judul = input('Judul lagu: ')
            if judul == '':
                print("Judul tidak boleh kosong.")
            elif judul in lagu_playlist:
                print(f"Lagu '{judul}' sudah ada.")
            else:
                print(f"Lagu '{judul}' ditambahkan.")

    elif pilihan == '3':
        if len(playlist) == 0:
            print("Belum ada playlist.")
        else:
            for nama_playlist, lagu_playlist in playlist.items():
                print(f"\nPlaylist: {nama_playlist}")
                if len(lagu_playlist) == 0:
                    print('  (belum ada lagu)')
                else:
                    for judul in lagu_playlist.items():
                        print(f"  - {judul}")

    elif pilihan == '6':
        nama_playlist = input('Playlist yang akan dihapus: ')
        try:
            del playlist[nama_playlist]
            print(f"Playlist '{nama_playlist}' berhasil dihapus.")
        except KeyError:
            print(f"Playlist '{nama_playlist}' tidak ditemukan.")

    elif pilihan == '7':
        print('Program Selesai')
        break
    else:
        print('Pilihan angka tidak ada di menu')