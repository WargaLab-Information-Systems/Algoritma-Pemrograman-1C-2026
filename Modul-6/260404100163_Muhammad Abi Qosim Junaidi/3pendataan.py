def evaluasi(status, ram):
    if status.lower() == "normal" and ram >= 8:
        return "Layak"
    else:
        return "Tidak Layak"

# Menyimpan data PC
data_pc = []

# Memasukkan jumlah PC
jumlah = int(input("Masukkan jumlah PC: "))

# Input data PC
for i in range(jumlah):
    print("Data PC ke-", i + 1)

    nama = input("Nama PC: ")
    status = input("Status (Normal/Rusak): ")
    ram = input("Kapasitas RAM: ")

    data_pc.append([nama, status, ram])

# Memeriksa kelayakan PC
print("=== HASIL EVALUASI ===")

for pc in data_pc:

    try:
        hasil = evaluasi(pc[1], int(pc[2]))

    except ValueError:
        hasil = "Format RAM Kacau"

    # Mencetak hasil dengan manipulasi string
    print('{ "PC": "' + pc[0] +
          '", "Status": "' + hasil + '" }')

print("Program selesai.")
