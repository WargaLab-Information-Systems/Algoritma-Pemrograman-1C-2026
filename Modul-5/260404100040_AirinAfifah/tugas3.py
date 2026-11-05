nama = input("nama mahasiswa: ")
tugas = float(input("nilai tugas: "))
uts = float(input("nilai UTS: "))
uas = float(input("nilai UAS: "))

def hitung_nilai(nama, tugas, uts, uas):
    nilai_akhir = (0.30 * tugas) + (0.30 * uts) + (0.40 * uas)
    
    if nilai_akhir >= 85:
        grade = "A"
        status = "lulus"
    elif nilai_akhir >= 70:
        grade = "B"
        status = "lulus"
    elif nilai_akhir >= 55:
        grade = "C"
        status = "lulus"
    else:
        grade = "D"
        status = "tidak lulus"

    print("\nnama:", nama)
    print(f"nilai akhir: {nilai_akhir:.2f}")
    print("grade:", grade)
    print("status:", status)

hitung_nilai(nama, tugas, uts, uas)