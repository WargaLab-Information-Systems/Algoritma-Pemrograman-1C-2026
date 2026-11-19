playlist = {}
while True:
    print("\n=== MENU PLAYLIST MUSIK ===")
    print("1. Buat playlist")
    print("2. Tambah lagu")
    print("3. Tampilkan playlist")
    print("4. Cari lagu")
    print("5. Hapus lagu")
    print("6. Hapus playlist")
    print("7. Keluar")
    try:
        pilihan = int(input("Pilih menu: "))
        menu = {
            1: "buat",
            2: "tambah",
            3: "tampil",
            4: "cari",
            5: "hapus_lagu",
            6: "hapus_playlist",
            7: "keluar"
        }
        perintah = menu[pilihan]
        try:
            if perintah == "buat":
                nama = input("Nama playlist: ")
                playlist[nama] = {}
            elif perintah == "tambah":
                nama = input("Nama playlist: ")
                lagu = input("Judul lagu: ")
                penyanyi = input("Nama penyanyi: ")
                playlist[nama][lagu] = penyanyi
            elif perintah == "tampil":
                print(playlist)
            elif perintah == "cari":
                lagu = input("Judul lagu: ")
                hasil = [
                    (nama, penyanyi)
                    for nama, isi in playlist.items()
                    for judul, penyanyi in isi.items()
                    if judul == lagu
                ]
                print(hasil)
            elif perintah == "hapus_lagu":
                nama = input("Nama playlist: ")
                lagu = input("Judul lagu: ")
                playlist[nama].pop(lagu)
            elif perintah == "hapus_playlist":
                nama = input("Nama playlist: ")
                playlist.pop(nama)
            elif perintah == "keluar":
                break
        except KeyError:
            print("Playlist atau lagu tidak ditemukan!")
    except ValueError:
        print("Masukkan pilihan berupa angka!")