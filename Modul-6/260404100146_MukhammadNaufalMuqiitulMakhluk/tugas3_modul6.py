data_pc = []

def cek_pc(status, ram):
    if status == "normal" and ram >= 8:
        return "Layak"
    else:
        return "Tidak Layak"


jumlah = int(input("Masukkan jumlah PC: "))

for i in range(jumlah):
    print("\nData PC ke-", i + 1)

    nama = input("Nama PC: ")
    status = input("Status PC (normal/rusak): ")
    ram = input("Kapasitas RAM (GB): ")

    data_pc.append([nama, status, ram])


print("\nHASIL EVALUASI PC")

for pc in data_pc:
    try:#digunakan untuk menjalankan kode yang kemungkinan mengalami error
        ram = int(pc[2])

        hasil = cek_pc(pc[1], ram)

    except ValueError:#untuk menangkap error
        hasil = "Format RAM Kacau"

    print('{ "PC": "' + pc[0] + '", "Status": "' + hasil + '" }')