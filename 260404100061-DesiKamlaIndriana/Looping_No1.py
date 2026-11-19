print("=== Penumpang Bus ===")
Jumlah_penumpang = 0
Total_jarak = 0
Rata_rata_jarak = 0
Jarak_terjauh = 0
Total_pendapatan = 0

while True:
    Jarak = int(input("Masukkan Jarak =  "))
    if Jarak == 0:
        break
    elif Jarak < 0:
        print("Tidak Valid")
        continue
    elif Jarak <= 5:
        Tarif_bus = 3000
        print("Tarif A bus = ", Tarif_bus)
    elif Jarak >=6 and Jarak <=15:
        Tarif_bus = 3000+(Jarak - 5)*1000
        print("Tarif B bus = ", Tarif_bus)
    elif Jarak > 15:
        Tarif_bus = 13000+(Jarak - 15)*500
        print("Tarif C bus = ", Tarif_bus)
    Jumlah_penumpang = Jumlah_penumpang + 1
    print("Jumlah penumpang = ", Jumlah_penumpang)
    Tarif_setelah_diskon = Tarif_bus
    if Jumlah_penumpang % 5 == 0:
        print("Dapat diskon 50%")
        Diskon = Tarif_bus * 50/100
        print("Besar diskon = ", Diskon)
        Tarif_setelah_diskon = Tarif_bus - Diskon
        print("Tarif bus setelah diskon = ", Tarif_setelah_diskon)
    Total_pendapatan = Total_pendapatan + Tarif_setelah_diskon
    print("Total Pendapatan = ", Total_pendapatan)
    Total_jarak = Total_jarak + Jarak
    if Jarak > Jarak_terjauh:
        Jarak_terjauh = Jarak
print("Total jarak = ", Total_jarak)
Rata_rata_jarak = Total_jarak / Jumlah_penumpang
print("Rata-rata jarak = ", Rata_rata_jarak)
print("Jarak terjauh = ", Jarak_terjauh)
    
    


    

    
    


    