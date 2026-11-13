def evaluasi_kelayakan(pc):
    ram = int(pc[2])
    if pc[1].lower() == "normal" and ram >= 8:
        return "Layak"
    return "Tidak Layak"

while True:
    try:
        jumlah = int(input("Jumlah PC yang akan didata: "))
        if jumlah > 0:
            break
    except ValueError:
        pass
    print("Jumlah harus bilangan bulat positif, masukkan ulang.")

inventaris = []
for i in range(jumlah):
    print(f"\nData PC ke-{i + 1}")
    nama = input("Nama PC              : ")
    status = input("Status (Normal/Rusak): ")
    ram = input("Kapasitas RAM (GB)   : ")
    inventaris.append([nama, status, ram])

print("\n=== Hasil Evaluasi Kelayakan PC ===")
for pc in inventaris:
    try:
        kelayakan = evaluasi_kelayakan(pc)
    except ValueError:
        kelayakan = "Format RAM Kacau"
    print('{ "PC": "'+ pc[0] +'", "Status": "'+ kelayakan +'" }')
