def nilai_akhir(nama, tugas, uts, uas):
    akhir = int (0.3 * tugas + 0.3 * uts + 0.4 * uas)

    if akhir >= 85:
        grade = "A"
    elif akhir >= 70:
        grade = "B"
    elif akhir >= 55:
        grade = "C"
    else:
        grade = "D"

    if grade == "D":
        status = "Tidak lulus"
    else:
        status = "Lulus"

    print("Nilai Akhir: ", akhir)
    print("Grade: ", grade)
    print("Status: ", status)

nama = input("Nama Mahasiswa: ")
tugas = float(input("Nilai tugas: "))
uts = float(input("Nilai UTS: "))
uas = float(input("Nilai UAS: "))
nilai_akhir(nama, tugas, uts, uas)
