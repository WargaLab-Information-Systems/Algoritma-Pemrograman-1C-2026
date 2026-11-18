def nilai_mahasiswa():
    nama = input("Masukkan nama: ")
    tugas = float(input("Nilai tugas: "))
    uts = float(input("Nilai UTS: "))
    uas = float(input("Nilai UAS: "))

    # Menghitung nilai akhir
    akhir = (tugas * 30/100) + (uts * 30/100) + (uas * 40/100)

    # Menentukan grade
    if akhir >= 85 and akhir <=100:
        grade = "A"
    elif akhir >= 70:
        grade = "B"
    elif akhir >= 55:
        grade = "C"
    else:
        grade = "D"

    # Menentukan kelulusan
    if grade == "D":
        status = "Tidak Lulus"
    else:
        status = "Lulus"

    # Menampilkan hasil
    print("\n=== HASIL NILAI ===")
    print("Nama:", nama)
    print("Nilai Akhir:", akhir)
    print("Grade:", grade)
    print("Status:", status)

nilai_mahasiswa()
