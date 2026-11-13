def evaluasi(pc):
    ram = int(pc[2])
    if pc[1] == "Normal" and ram >= 8:
        return "Layak"
    return "Tidak Layak"

jumlah = int(input("Jumlah PC: "))
data = []
for i in range(jumlah):
    nama = input("Nama PC: ")
    status = input("Status (Normal/Rusak): ")
    ram = input("RAM (GB): ")
    data.append([nama, status, ram])

for pc in data:
    try:
        hasil = evaluasi(pc)
    except ValueError:
        hasil = "Format RAM Kacau"
    print('{ "PC": "' + pc[0] + '", "Status": "' + hasil + '" }')