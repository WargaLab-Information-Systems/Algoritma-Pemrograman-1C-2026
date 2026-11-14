
data_pc = []

jumlah = int(input("Masukkan jumlah PC: "))

for i in range(jumlah):
    print("\nData PC ke-", i + 1)

    nama = input("Nama PC: ")
    status = input("Status (Normal/Rusak): ")
    ram = input("Kapasitas RAM (GB): ")

    data_pc.append([nama, status, ram])


def evaluasi_pc(status, ram):
    if status.strip().lower() == "normal" and float(ram) >= 8:
        return "Layak"
    else:
        return "Tidak Layak"


print("\nHasil Evaluasi Inventaris PC:")

for pc in data_pc:
    try:
        hasil = evaluasi_pc(pc[1], pc[2])

    except (ValueError, TypeError):
        hasil = "Format RAM Kacau"

    output = '{ "PC": "' + pc[0] + '", "Status": "' + hasil + '" }'

    print(output)
