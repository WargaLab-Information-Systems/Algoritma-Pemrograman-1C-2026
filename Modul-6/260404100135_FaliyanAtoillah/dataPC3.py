Data_pc = []

while True:
    jumlah_pc = int(input("Masukkan jumlah PC: "))
    if jumlah_pc <= 0:
        print("Jumlah PC")
    else:
        break

Data_pc = []
for i in range(jumlah_pc):
    print("\nData PC ke-", i + 1)

    nama = input("Nama PC: ")
    status = input("Status (Normal/Rusak): ")
    ram = input("Kapasitas RAM (GB): ")

    Data_pc.append([nama, status, ram])

#untuk panggil kembali dan periksa
def cek_pc(status, ram):
    if status == "Normal" and int(ram) >= 8:
        return "Layak"
    else:
        return "Tidak Layak"


for pc in Data_pc:
    try:
        hasil = cek_pc(pc[1], pc[2])
#nangani ketika try error
    except:
        hasil = "Format RAM Kacau"

    print('{ "PC": "' + pc[0] + '", "Status": "' + hasil + '" }')