jarak_terjauh=0
jumlah_penumpang=0
total_jarak=0
total_pendapatan=0

while True:
    jarak=int(input("masukkan jarak(0 untuk selesai):"))
    
    if jarak==0:
        break
    if jarak <0:
        print("jarak tidak valid,ulangi!")
        continue

    jumlah_penumpang=jumlah_penumpang+1
    total_jarak=total_jarak+jarak

    if jarak > jarak_terjauh:
        jarak_terjauh=jarak
        
    if jarak <=5:
        tarif=3000
    elif jarak <=15:
        tarif=3000+(jarak-5)*1000
    else:tarif=13000+(jarak-15)*500

    if jumlah_penumpang % 5==0:
        tarif=tarif//2
        print("diskon 50%")

    print("tarif penumpang:", tarif)
    total_pendapatan=total_pendapatan + tarif
    
    
print("Laporan Akhir")
print("jumlah penumpang:",jumlah_penumpang )
if jumlah_penumpang>0:
    rata_jarak=total_jarak/jumlah_penumpang
    print("total pendapatan:Rp", total_pendapatan)
    print("jarak terjauh:",jarak_terjauh,"km")
    print("rata-rata jarak:", rata_jarak, "km") 
else:
    print("tidak ada penumpang")

