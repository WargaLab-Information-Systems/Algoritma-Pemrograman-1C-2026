def nilai_mahasiswa(nama, tugas, uts, uas):
    nilai_akhir = (tugas * 0.30) + (uts * 0.30) + (uas * 0.40)

    if nilai_akhir >= 85:
        grade = "A"
    elif nilai_akhir >= 70:
        grade = "B"
    elif nilai_akhir >= 55:
        grade = "C"
    else:
        grade = "D"

    if grade == "A" or grade == "B" or grade == "C":
        status = "Lulus"
    else:
        status = "Tidak Lulus"


    print("Nama Mahasiswa :", nama)
    print("Nilai Tugas    :", tugas)
    print("Nilai UTS      :", uts)
    print("Nilai UAS      :", uas)
    print("Nilai Akhir    :", nilai_akhir)
    print("Grade          :", grade)
    print("Status         :", status)

nama = input("Masukkan nama mahasiswa: ")
while True:
    tugas = float(input("Masukkan nilai tugas: "))
    if tugas >= 0 and tugas <= 100:
        break
    print("Nilai tugas harus antara 0 dan 100, ulangi.")

while True:
    uts = float(input("Masukkan nilai UTS: "))
    if uts >= 0 and uts <= 100:
        break
    print("Nilai UTS harus antara 0 dan 100, ulangi.")

while True:
    uas = float(input("Masukkan nilai UAS: "))
    if uas >= 0 and uas <= 100:
        break
    print("Nilai UAS harus antara 0 dan 100, ulangi.")

nilai_mahasiswa(nama, tugas, uts, uas)