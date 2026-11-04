def munculin(*objek):
    print(*objek)

def input_nama():
    nama = input("Masukkan nama mahasiswa: ")
    return nama


def input_nilai():
    nilai = float(input("Masukkan nilai mahasiswa: "))
    return nilai

def tentukan_grade(nilai):
    if nilai >= 85:
        return "A"
    elif nilai >= 75:
        return "B"
    elif nilai >= 65:
        return "C"
    elif nilai >= 50:
        return "D"
    else:
        return "E"

def cek_kelulusan(nilai):
    if nilai >= 65:
        return "LULUS"
    else:
        return "TIDAK LULUS"

def tampilkan_hasil(nama, nilai, grade, status):
    munculin("\n===== HASIL NILAI MAHASISWA =====")
    munculin("Nama       :", nama)
    munculin("Nilai      :", nilai)
    munculin("Grade      :", grade)
    munculin("Status     :", status)

def main():
    nama = input_nama()
    nilai = input_nilai()

    grade = tentukan_grade(nilai)
    status = cek_kelulusan(nilai)

    tampilkan_hasil(nama, nilai, grade, status)

main()