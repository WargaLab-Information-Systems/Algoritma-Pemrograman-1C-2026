print("=== PROGRAM KASIR BUS SIDOARJO ===")

jumlah_penumpang = 0
total_pendapatan = 0
jarak_terjauh = 0
total_jarak = 0

while True:
    jarak = float(input("Masukkan jarak tempuh (km) (Ketik 0 untuk selesai): "))
    
    if jarak == 0:
        break
    elif jarak < 0:
        print("Peringatan: Jarak tidak valid! Masukkan angka positif.")
        continue
        
    jumlah_penumpang = jumlah_penumpang + 1
    total_jarak = total_jarak + jarak
    
    if jarak > jarak_terjauh:
        jarak_terjauh = jarak
        
    if jarak <= 5:
        tarif = 3000
    elif jarak <= 15:
        tarif = 3000 + (jarak - 5) * 1000
    else:
        tarif = 13000 + (jarak - 15) * 500
        
    if jumlah_penumpang % 5 == 0:
        tarif = tarif * 0.5
        print("Info: Penumpang ke-", jumlah_penumpang, "mendapat diskon 50%!")
        
    total_pendapatan = total_pendapatan + tarif

print("==== LAPORAN AKHIR ====")
if jumlah_penumpang > 0:
    rata_rata_jarak = total_jarak / jumlah_penumpang
    print("Jumlah Penumpang   :", jumlah_penumpang)
    print("Total Pendapatan   : Rp", total_pendapatan)
    print("Jarak Terjauh      :", jarak_terjauh)
    print("Rata-rata Jarak    :", rata_rata_jarak)
else:
    print("Tidak ada data penumpang yang dimasukkan.")