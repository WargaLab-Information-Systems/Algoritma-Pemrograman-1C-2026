print("= JADWAL SHIFT ASISTEN  =")
#list kosong nama asisten
asisten_awal = []
#untuk input brp nma
while True:
    nama = input("Masukkan nama asisten ('cukup' untuk berhenti): ")

    if nama == "cukup":
        break
#masukan nama pada list
    asisten_awal.append(nama)

asisten_awal = tuple(asisten_awal)

tambahan = input("Masukkan nama asisten tambahan: ")

asisten_akhir = asisten_awal + (tambahan,)

hari_list = []
#input brp hari
while True:
    nama_hari = input("Masukkan hari tugas ('cukup' untuk berhenti): ")

    if nama_hari == "cukup":
        break
#nmbah hr pda hrilist
    hari_list.append(nama_hari)

hari_tugas = tuple(hari_list)

nama_izin = input("Nama asisten yang dikecualikan: ")
hari_izin = input("Hari yang dikecualikan: ")

print("\nJadwal Shift Asisten:")
#pke 2 for untuk menggabungkan nama asisten dan hari tugas
for nama in asisten_akhir:
    for h in hari_tugas:
#data pengcualian
        if nama == nama_izin and h == hari_izin:
            #melanjutkan ke iterasi berikutnya 
            continue

        print(nama, "-", h)