def hitung_nilai(nama, tugas, uts, uas):
    nilai_akhir = (30 * tugas + 30 * uts + 40 * uas) / 100

    if nilai_akhir >= 85:
        grade = "A"
    elif nilai_akhir >= 70:
        grade = "B"
    elif nilai_akhir >= 55:
        grade = "C"
    else:
        grade = "D"

    if grade == "D":
        status = "Tidak Lulus"
    else:
        status = "Lulus"

    print(f"\nNama mahasiswa: {nama}")
    print(f"Nilai tugas   : {tugas:.2f}")
    print(f"Nilai UTS     : {uts:.2f}")
    print(f"Nilai UAS     : {uas:.2f}")
    print(f"Nilai akhir   : {nilai_akhir:.2f}")
    print(f"Grade         : {grade}")
    print(f"Status        : {status}")


def baca_nilai(keterangan):
    while True:
        nilai = float(input(f"Masukkan nilai {keterangan} (0-100): "))
        if 0 <= nilai <= 100:
            return nilai
        print("Nilai harus berada pada rentang 0 sampai 100, masukkan ulang.")

while True:
    nama = input("Masukkan nama mahasiswa: ")
    if nama != "":
        break
    print("Nama tidak boleh kosong, masukkan ulang.")

nilai_tugas = baca_nilai("tugas")
nilai_uts = baca_nilai("UTS")
nilai_uas = baca_nilai("UAS")

hitung_nilai(nama, nilai_tugas, nilai_uts, nilai_uas)
