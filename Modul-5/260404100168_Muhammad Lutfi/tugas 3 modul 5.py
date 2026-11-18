def nilai_mahasiswa(nama, tugas, uts, uas):
    total_nilai = tugas * 0.3 + uts * 0.3 + uas * 0.4

    if total_nilai >= 85:
        grade = "A"
    elif total_nilai >= 70:
        grade = "B"
    elif total_nilai >= 55:
        grade = "C"
    elif total_nilai >= 40:
        grade = "D"

    if grade == "D":
        status = "Tidak Lulus"
    else:
        status = "Lulus"

    print("\nNama Mahasiswa:", nama)
    print("total nilai:", total_nilai)
    print("Grade:", grade)
    print("Status:", status)

nama = input("Masukkan nama mahasiswa: ")
tugas = float(input("Masukkan nilai tugas: "))  
uts = float(input("Masukkan nilai UTS: "))
uas = float(input("Masukkan nilai UAS: "))

nilai_mahasiswa(nama, tugas, uts, uas)