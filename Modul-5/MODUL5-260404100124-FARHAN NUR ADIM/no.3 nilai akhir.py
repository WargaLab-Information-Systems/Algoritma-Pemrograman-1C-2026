def hitung_nilai ():
    nama = str(input("Masukkan nama mahasiswa   : "))
    tugas = float(input("Masukkan nilai tugasnya   : "))
    uts = float(input("Masukkan nilai UTS nya    : "))
    uas= float(input("Masukkan nilai UAS nya    : "))

    nilai_akhir = ((30/100)*tugas + (30/100)*uts + (40/100)*uas)

    if nilai_akhir >=85:
        grade = "A"
        status = "Lulus"
    elif nilai_akhir >=70:
        grade = "B"
        status = "Lulus"
    elif nilai_akhir >=55:
        grade = "C"
        status = "Lulus"
    else:
        grade = "D"
        status = "Tidak Lulus"

    print("\n==HASIL==")
    print(f"Nama Mahasiswa  : {nama}")
    print(f"Nilai Tugas     : {tugas}")
    print(f"Nilai UTS       : {uts}")
    print(f"Nilai UAS       : {uas}")
    print(f"Nilai Akhir     : {nilai_akhir}")
    print(f"Grade           : {grade}")
    print(f"Status          : {status}")

hitung_nilai()