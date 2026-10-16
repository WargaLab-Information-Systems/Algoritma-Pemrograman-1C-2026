pin = int(input("Masukkan 3 digit PIN: "))
jam = int(input("Masukkan jam kedatangan (0-23): "))

d1 = pin // 100
d2 = (pin // 10) % 10
d3 = pin % 10

if pin % 5 == 0:
    if jam < 12:
        status_akses = "Garasi Pagi Terbuka"
    else:
        status_akses = "Garasi Malam Terbuka, Lampu Dinyalakan"
elif pin % 2 == 0:
    if (d1 + d3) == d2:
        status_akses = "Garasi VIP Terbuka Khusus Bos"
    else:
        status_akses = "Kode Genap Ditolak, Alarm Berbunyi!"
else:
    status_akses = "Akses ditolak sepenuhnya"

status_kamera = "Mode Malam Merekam" if jam > 18 else "Mode Siang Standby"

print("Digit PIN:", d1, d2, d3)
print("Status Akses:", status_akses)
print("Status Kamera:", status_kamera)

# 1. Akses Pagi: pin: 125, Jam: 10 Output: Garasi Pagi Terbuka & Mode Siang Standby.   
# 2. Akses Malam: pin: 250, Jam: 20 Output: Garasi Malam Terbuka, Lampu Dinyalakan & Mode Malam Merekam.   
# 3. VIP Bos: pin: 132, Jam: 14  Output: Garasi VIP Terbuka Khusus Bos & Mode Siang Standby.   
# 4. Penyusup Genap: pin: 284, Jam: 22 Output: Kode Genap Ditolak, Alarm Berbunyi! & Mode Siang Standby.