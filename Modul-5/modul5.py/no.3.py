def nilai_mahasiswa(nama, tugas, uts, uas):
    nilai_akhir=(tugas* 30/100)+(uts *30/100)+ (uas * 40/100)
    if nilai_akhir >= 85:
        grade="A"
    elif nilai_akhir >=70:
        grade= "B"
    elif nilai_akhir >= 55:
        grade="C"
    else:
        grade="D"

    if grade == "A" or grade =="B" or grade =="C":
        status="Lulus"
    else:
        status= "tidak lulus"
    print ("\n===HASIL NILAI MAHASISWA===")
    print ( "Nama mahasiswa:", nama )
    print("Nilai tugas:", tugas)
    print("Nilai uts:", uts)
    print("Nilai uas:", uas)
    print("Nilai akhir:", nilai_akhir)
    print("grade:",grade)
    print("status:", status)
nama= input ("Masukkan nama mahasiswa:")
tugas= float(input("Masukkan nilai tugas:"))
uts= float(input("Masukkan nilai uts:"))
uas= float (input("Masukkan nilai uas:"))
nilai_mahasiswa(nama, tugas, uts, uas)