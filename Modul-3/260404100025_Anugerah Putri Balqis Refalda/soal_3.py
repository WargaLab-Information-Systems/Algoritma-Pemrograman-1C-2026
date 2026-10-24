jumlah_A=0
jumlah_B=0
jumlah_C=0
jumlah_D=0
jumlah_E=0
total_nilai=0
nilai_tertinggi=-1
nilai_terendah=101
for i in range(1,11):
    print("\nMahasiswa ke-",i)
    nama=input(" nama mahasiswa: ")
    tugas= float(input("nilai tugas: "))
    uts= float(input("nilai UTS: "))
    uas= float(input ("nilai uas: "))
nilai_akhir= tugas*30/100+ uts*30/100+ uas*40/100
if nilai_akhir>= 85:
    kategori= "A"
    jumlah_A+=1
elif nilai_akhir>=75:
    kategori="B"
    jumlah_B+=1
elif nilai_akhir >=65:
    kategori="C"
    jumlah_C+= 1
elif nilai_akhir>=50:
    kategori="D"
    jumlah_D+=1
else:
    kategori= "E"
    jumlah_E +=1
    print("nama:",nama)
    print("nilai tugas:", tugas)
    print("nilai uts:",uts)
    print("nilai uas:",uas)
    print ("nilai_akhir:",nilai_akhir)
    print("kategori:", kategori)
total_nilai+=nilai_akhir
if nilai_akhir>nilai_tertinggi:
    nilai_tertinggi=nilai_akhir
    nama_tertinggi=nama
if nilai_akhir<nilai_terendah:
    nilai_terendah=nilai_akhir
    nama_terendah=nama
rata_rata=total_nilai/10
print("jumlah mahasiswa kategori A:", jumlah_A)
print("jumlah mahasiswa kategori B:", jumlah_B)
print("jumlah mahasiwa kategori C:", jumlah_C)
print("jumlah mahasiwa kategori D:", jumlah_D)
print("jumlah mahasiwa kategori E:", jumlah_E)
print("nilai tertinggi:", nilai_tertinggi)
print("mahasiswa dengan nama tertinggi:", nama_tertinggi)
print("nilai terendah:", nilai_terendah)
print("mahasiswa dengan nama terendah:", nama_terendah)
print("rata rata nilai akhir:", rata_rata)