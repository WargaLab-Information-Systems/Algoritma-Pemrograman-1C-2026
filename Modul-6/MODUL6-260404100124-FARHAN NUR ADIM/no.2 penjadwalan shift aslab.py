aslab_awal = []

while True:
    nama = str(input("Masukkan nama-nama asisten awal: "))
    if nama == "cukup":
        break

    aslab_awal.append(nama)

aslab_awal = tuple(aslab_awal)

nama2 = str(input("Masukkan nama asisten tambahan yg mendadak gabung: "))

aslab_akhir = aslab_awal + (nama2,)
print("Nama-nama asisten laboratorium: ",aslab_akhir)

hari = []

while True:
    nama_hari = str(input("\nMasukkan nama-nama hari tugas: "))
    if nama_hari == "cukup":
        break

    hari.append(nama_hari)

hari = tuple(hari)
print("Nama-nama hari tugas: ",hari)

pengecualian_aslab = str(input("\nMasukkan nama asisten yg menjadi pengecualian: "))
pengecualian_hari = str(input("Masukkan nama hari yg menjadi pengecualian: "))

for aslab in aslab_akhir:
    for nama_hari in hari:
        if aslab==pengecualian_aslab and nama_hari==pengecualian_hari:
            continue
        print("Kombinasi shift: ",aslab,"--",nama_hari)