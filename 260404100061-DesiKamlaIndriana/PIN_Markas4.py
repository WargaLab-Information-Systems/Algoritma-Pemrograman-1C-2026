print("=== PIN membuka markas ===")
Digit1 = int(input("Masukkan PIN Digit1 = "))
Digit2 = int(input("Masukkan PIN Digit2 = "))
Digit3 = int(input("Masukkan PIN Digit3 = "))
print("PIN = ", Digit1, Digit2, Digit3)
Jam_kedatangan = int(input("Jam Kedatangan = "))
if Digit3 % 5 == 0:
    if Jam_kedatangan < 12:
        print("Garasi Pagi Terbuka")
    else:
        print("Garasi Malam Terbuka, lampu dinyalakan")
elif Digit3 % 2 == 0:
    if (Digit1 + Digit3) == Digit2:
        print("Garasi VIP Terbuka Khusus Bos")
    else:
        print("Kode Genap Ditolak, Alarm Berbunyi!")
else:
    print("Akses ditolak sepenuhnya")
print("Status Kamera CCTV = Mode Malam Merekam"if Jam_kedatangan > 18 else "Status Kamera CCTV = Mode Siang Standby")