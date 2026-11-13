daftar = []
while True:
    nama = input("Nama calon anggota: ")
    if nama == "selesai":
        break
    daftar.append(nama)

for nama in daftar:
    if nama == "admin" or len(nama) < 4:
        print(nama, "tidak valid")

penyusup = input("Nama penyusup: ")
if penyusup in daftar:
    daftar.remove(penyusup)
else:
    print("Nama tidak ditemukan")
print(daftar)