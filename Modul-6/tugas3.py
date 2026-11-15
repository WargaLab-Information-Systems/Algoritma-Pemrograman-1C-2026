def evaluasi_pc(status, ram):
    if status == "normal" and ram >= 8:
        return "Layak"
    else:
        return "Tidak Layak"

data_pc = []

jumlah_pc = int(input("Masukkan jumlah PC: "))
for i in range(jumlah_pc):
    print("Data PC ke-", i + 1)

    nama = input("Masukkan nama PC: ")
    status = input("Masukkan status (normal/rusak): ")
    ram = input("Masukkan kapasitas RAM (GB): ")

    data_pc.append([nama, status, ram])

print("Hasil Evaluasi kelayakan PC:")

for pc in data_pc:
    nama = pc[0]
    status = pc[1]
    ram = pc[2]

    try:
        hasil = evaluasi_pc(status, int(ram))

    except (ValueError, TypeError):
        hasil = "Format RAM Kacau"

    print('{ "PC": "' + nama + '", "Status": "' + hasil + '" }')
