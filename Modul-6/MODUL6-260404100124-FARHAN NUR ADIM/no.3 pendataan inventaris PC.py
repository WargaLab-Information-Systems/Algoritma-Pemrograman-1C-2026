data_pc = []

jumlah_pc = int(input("Masukkan jumlah PC: "))

for i in range (jumlah_pc):
    print(f"\nData PC ke-{i+1}")
    nama = input("Masukkan nama PC nya: ")
    status = input("Masukkan status PC nya: ")
    ram = input("Masukkan kapasitas RAM nya (GB): ")

    data_pc.append([nama,status,ram])
print(data_pc)

def evaluasi_pc (status,ram):
    if status=="normal" and int(ram) >= 8:
        return "Layak"
    else:
        return "Tidak Layak"

print("\nHasil evaluasi inventaris PC: ")

for i in data_pc:
    try:
        hasil = evaluasi_pc(i[1],i[2])
    except:
        hasil = "Format RAM Kacau"

    print('{"PC": "' + i[0] + '", "Status": "'+ hasil +'"}')