def hitung_nilai(tugas,uts,uas):
    nilai=(0.3*tugas) + (0.3*uts) + (0.4*uas)
    return nilai
def cek_kategori(nilai):
    if nilai >=85:
        kategori= "A"
    if nilai >=70:
        kategori= "B"
    if nilai >= 55:
        kategori= "C"
    else:
        kategori= "D"
    return kategori

cek_lulus=lambda kat:"LULUS" if kat=="A" or kat=="B" or kat=="C" else"TIDAK LLULUS"

nama=input("masukkan nama:")
tugas=float(input("masukkan nilai:"))
uts=float(input("masukkan nilai:"))
uas=float(input("masukkan nilai:"))

akhir=hitung_nilai(tugas,uts,uas)
kategori=cek_kategori (akhir)
ket=cek_lulus(kategori)

print("HASIL")
print("nama:", nama)
print("nilai_akhir:", akhir)
print("kategori:", kategori)
print("keterangan:", ket)
