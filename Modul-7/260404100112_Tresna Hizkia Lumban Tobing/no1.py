
tugas = {}
while True:
    print("\n=== TO-DO LIST ===")
    print("1. Tambah tugas")
    print("2. Tampilkan tugas")
    print("3. Tandai tugas selesai")
    print("4. Hapus tugas")
    print("5. Jumlah tugas")
    print("6. Keluar")
    try:
        pilih = int(input("Pilih menu: "))
        try:
            {
                1: lambda: tugas.update({
                    input("Nama tugas: "): "Belum selesai"
                }),
                2: lambda: print(tugas),
                3: lambda: tugas.update({
                    input("Nama tugas: "): "Selesai"
                }),
                4: lambda: tugas.pop(
                    input("Nama tugas: ")
                ),
                5: lambda: print(
                    "Selesai:", list(tugas.values()).count("Selesai"),
                    "\nBelum selesai:", list(tugas.values()).count("Belum selesai")
                ),
                6: lambda: exit(),
            }[pilih]()
        except KeyError:
            print("Menu atau tugas tidak ditemukan!")
    except ValueError:
        print("Masukkan angka yang benar!")
