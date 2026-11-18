inventaris = []

jumlah = int(input("Masukkan jumlah PC: "))

for i in range(jumlah):
    print("\nData PC ke-", i + 1)

    nama = input("Nama PC: ")
    status = input("Status (Normal/Rusak): ")
    ram = input("Kapasitas RAM: ")

    inventaris.append([nama, status, ram])

def evaluasi(status, ram):
    if status == "Normal" and ram >= 8:
        return "Layak"
    else:
        return "Tidak Layak"

print("\n=== Hasil Evaluasi Inventaris ===")

for pc in inventaris:
    try:
        hasil = evaluasi(pc[1], int(pc[2]))
    except ValueError:
        hasil = "Format RAM Kacau"

    print('{ "PC": "' + pc[0] + '", "Status": "' + hasil + '" }')