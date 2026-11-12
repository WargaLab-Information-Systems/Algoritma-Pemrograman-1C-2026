def evaluasi_pc(data):
    if data[1] == "normal" and int(data[2]) >= 8:
        return "layak"
    else:
        return "tidak layak"

inventaris = []

jumlah = int(input("jumlah PC: "))

for i in range(jumlah):
    print("\ndata PC ke-", i + 1)

    nama = input("nama PC: ")
    status = input("status (normal/rusak): ")
    ram = input("kapasitas RAM (GB): ")

    inventaris.append([nama, status, ram])

print("\nhasil evaluasi:")

for pc in inventaris:
    try:
        kelayakan = evaluasi_pc(pc)

    except ValueError:
        kelayakan = "format RAM kacau"

    hasil = '{ "PC": "' + pc[0] + '", "status": "' + kelayakan + '" }'

    print(hasil)