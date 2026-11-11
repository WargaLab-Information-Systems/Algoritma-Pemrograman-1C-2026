print("====== Sistem Penjadwalan Shift Asisten Laboratorium ======")

print("===== Nama Asisten Lab =====")
Data_asisten_Lab = ()
while True:
    Nama = (input("Nama Aslab : "))
    if Nama.lower() == "cukup":
        break
    else:
        Data_asisten_Lab = Data_asisten_Lab + (Nama,)
print("Data nama asisten lab: ", Data_asisten_Lab)

Aslab_tambahan = (input("Aslab tambahan : "))
Data_asisten_Lab_new = Data_asisten_Lab + (Aslab_tambahan,)
print("Data nama asisten lab: ", Data_asisten_Lab_new)

print("===== Hari Tugas Asisten Lab =====")
Hari = ()
while True:
    Hari_tugas = (input("Hari: "))
    if Hari_tugas.lower() == "cukup":
        break
    else:
        Hari = Hari + (Hari_tugas,)
print("Hari: ", Hari)

print("====== Kombinasi shift ======")
for i in Hari:
    for j in Data_asisten_Lab_new:
        print("Kombinasi shift aslab: ", i, j)


#Pengecualian shift 
print("====== Shift pengecualian ======")
Nama_aslab_absen = (input("Nama Aslab Absen : "))
Hari_spesifik = (input("Hari : "))

print("Hari: ", Hari)
print("====== Kombinasi shift new ======")
for i in Hari:
    for j in Data_asisten_Lab_new:
        if j.lower() == Nama_aslab_absen.lower() and i.lower() == Hari_spesifik.lower():
            continue                 #lewati untuk lanjut ..berikutnya
        print("Kombinasi shift aslab: ", i, j)

