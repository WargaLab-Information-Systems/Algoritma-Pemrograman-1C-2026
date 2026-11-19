playlist = {}

while True:
    print("1.Buat 2.Tambah 3.Tampil 4.Cari 5.Hapus lagu 6.Hapus playlist 0.Keluar")
    pilih = input("Menu: ")

    if pilih == "1":
        nama = input("Nama playlist: ")
        playlist[nama] = {}
    elif  pilih == "2":
        nama = input("Nama playlist: ")
        if nama in playlist:
             judul = input("Judul lagu: ")
             penyanyi = input("Penyanyi: ")
             playlist[nama][judul] = penyanyi
        else:
             print("Playlist tidak ada")
    elif pilih == "3":
        for nama in playlist:
             print(nama)
             for judul in playlist[nama]:
                  print("-", judul, ":", playlist[nama][judul])
    elif pilih == "4":
            nama = input("Judul lagu: ")
            for nama in playlist:
                if judul in playlist[nama]:
                     print("Ada di", nama)
    elif pilih == "5":
            nama = input("Nama playlist: ")
            judul = input("Judul lagu: ")
            if nama in playlist and judul in playlist[nama]:
                 del playlist[nama][judul]
            else:
                print("playlist atau lagu tidak ada")
    elif pilih == "6":
            nama = input("Nama playlist: ")
            if nama in playlist:
              del playlist[nama]
            else:
                print("Playlist tidak ada")
    elif pilih == "0":
        break