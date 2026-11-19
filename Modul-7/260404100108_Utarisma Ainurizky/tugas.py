tugas = {}

while True:
    print("1.Tambah 2.Tampil 3.Selesai 4.Hapus 5.Jumlah 0.Keluar")
    pilih = input("Menu: ")

    if pilih == "1":
        nama = input("Nama tugas: ")
        tugas[nama] = ("Belum")
    elif  pilih == "2":
        for nama, status in tugas.items():
            print(nama, "-", status)
    elif pilih == "3":
        nama = input("Nama tugas: ")
        if nama in tugas:
            tugas[nama] = "Selesai"
        else:
            print("Tugas tidak ada")
    elif pilih == "4":
            nama = input("Nama tugas: ")
            if nama in tugas:
                del tugas[nama]
            else:
                print("Tugas tidak ada")
    elif pilih == "5":
            selesai = list(tugas.values()).count("Selesai")
            print("Selesai: ", selesai)
            print("Belum: ", len(tugas) - selesai)
    elif pilih == "0":
         break