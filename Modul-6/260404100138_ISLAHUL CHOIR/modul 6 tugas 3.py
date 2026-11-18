
def evaluasi(status, ram):
    if ram >= 8 and status.lower() == "normal":
        return "Layak"
    else:
        return "Tidak Layak"



inventaris = []

jumlah = int(input("Masukkan jumlah PC: "))

for i in range(jumlah):
    print("Data PC ke-", i + 1)

    nama = input("Nama PC: ")
    status = input("Status (Normal/Rusak): ")
    ram = input("Kapasitas RAM (GB): ")

    try:
        hasil = evaluasi(status, float(ram))
    except:
        hasil = "Format RAM Kacau"

    inventaris.append([nama, status, ram, hasil])



print("HASIL INVENTARIS PC")

for pc in inventaris:
    print({
        "PC": pc[0],
        "Status": pc[3]
    })