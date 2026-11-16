jumlah_penumpang=0
pendapatan=0
total_jarak=0
jarak_terjauh=0
while True:
    jarak=float (input("Masukkan jarak tempuh(km):,0 untuk selesai:"))

    if jarak==0:
        break
    if jarak<0:
        print ("jarak tidak valid dan harus diulang tanpa dihitung sebagai penumpang:")
        continue
    jumlah_penumpang+=1
    total_jarak+=jarak
    if jarak<=5:
        tarif=3000
    elif jarak<=15:
        tarif=3000+(jarak-5)*1000
    else:
        tarif=13000+(jarak-15)*500
    if jumlah_penumpang %5==0:
        tarif=tarif*50/100
        print("diskon 50%")
    pendapatan+= tarif
    if jarak > jarak_terjauh:
        jarak_terjauh=jarak
    print("jarak:",jarak, "km")
    print("tarif yang harus dibayar:Rp", tarif)
    if jumlah_penumpang>0:
        rata_rata=total_jarak/jumlah_penumpang
    else:
     rata_rata=0
print("jumlah penumpang:",jumlah_penumpang)
print("Total pendapatan:Rp",pendapatan)
print("jarak terjauh",jarak_terjauh, ("km"))
print("rata rata jarak",rata_rata,("km"))





