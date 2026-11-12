def evaluasi_pc(pc):
    try:
        ram = int(pc[2])
        if pc[1] == "Normal" and ram >= 8:
            return "Layak"
        else:
            return "Tidak Layak"
    except ValueError:
        return "Format RAM Kacau"

jumlah = int(input("Masukkan jumlah PC : "))
inventaris = []
for i in range(jumlah):
    print("Data PC ke-" + str(i + 1))
    nama = input("  Nama PC               : ")
    status = input("  Status (Normal/Rusak) : ")
    ram = input("  Kapasitas RAM (GB)    : ")
    inventaris.append([nama, status, ram])

print("\nHasil evaluasi kelayakan PC:")
for pc in inventaris:
    kelayakan = evaluasi_pc(pc)
    print('{ "PC": "' + pc[0] + '", "Status": "' + kelayakan + '" }')
