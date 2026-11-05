print("=== Menghitung nilai akhir mahasiswa ===")

bobot_Tugas = 30/100
bobot_UTS = 30/100
bobot_UAS = 40/100
def data_mahasiswa():
    nama = input("Nama Mahasiswa : ")
    nilai_tugas = int(input("Nilai Tugas : "))
    nilai_UTS = int(input("Nilai UTS : "))
    nilai_UAS = int(input("Nilai UAS : "))

    nilai_akhir = (nilai_tugas * bobot_Tugas) + (nilai_UTS * bobot_UTS) + (nilai_UAS * bobot_UAS)
    print("Nilai akhir mahasiswa : ", nilai_akhir)
    return nilai_akhir

nilai_akhir = data_mahasiswa()
if nilai_akhir >= 85:
    print("======= Kategori : A -- LULUS =======")
elif nilai_akhir >= 70:
    print("======= Kategori : B -- LULUS =======")
elif nilai_akhir >= 55:
    print("======= Kategori : C -- LULUS =======")
else:
    print("======= Kategori : D -- TIDAK LULUS =======")


