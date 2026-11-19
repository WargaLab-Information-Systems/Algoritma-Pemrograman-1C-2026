print("==== Pendaftaran Anggota Robotika ====")

Data_nama_pendaftar = []
while True:
    Nama = (input("Nama: "))
    if Nama.lower() == "selesai":
        break
    else:
        Data_nama_pendaftar.append(Nama)
print("Data pendaftar club robotika = ", Data_nama_pendaftar)

for i in Data_nama_pendaftar:
    if i.lower() == "admin" or len(i) < 4:
        print("Nama", i, "tidak valid")
Nama_penyusup = input("Nama Yg dicurigai sebagai penyusup: ")
if Nama_penyusup in Data_nama_pendaftar:
    Data_nama_pendaftar.remove(Nama_penyusup)
    print(Data_nama_pendaftar)
else:
    print("Nama tidak ada didalam data pendaftaran")
