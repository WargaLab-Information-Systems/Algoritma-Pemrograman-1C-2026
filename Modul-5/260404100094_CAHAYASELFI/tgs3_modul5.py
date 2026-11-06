def nilai_mahasiswa(nama, tugas, uts, uas):
    akhir = (0.3 * tugas) + (0.3 * uts) + (0.4 * uas)
    
    if akhir >= 85:
        grade = "A"
    elif akhir >= 70:
        grade = "B"
    elif akhir >= 55:
        grade = "C"
    else:
        grade = "D"
        
    if grade == "D":
        status = "Tidak Lulus"
    else:
        status = "Lulus"
        
    print("\n--- Hasil Penilaian ---")
    print("Nama:", nama)
    print("Nilai Akhir:", akhir)
    print("Grade:", grade)
    print("Status:", status)

nama = input("Masukkan nama mahasiswa: ")
tugas = float(input("Masukkan nilai tugas: "))
uts = float(input("Masukkan nilai UTS: "))
uas = float(input("Masukkan nilai UAS: "))

nilai_mahasiswa(nama, tugas, uts, uas)