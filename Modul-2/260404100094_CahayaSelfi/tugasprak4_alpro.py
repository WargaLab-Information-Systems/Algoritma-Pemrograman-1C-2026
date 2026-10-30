# Program Jendral Wito Akses Pintu Garasi Markas CIA
pin = int(input("Masukkan 3 digit PIN garasi: "))
jam = int(input("Masukkan jam kedatangan (0-23): "))

digit1 = pin // 100
digit2 = (pin // 10) % 10
digit3 = pin % 10

if pin % 5 == 0:
    if jam < 12:
        pesan_akses = "Garasi Pagi Terbuka"
elif pin % 3 == 0:
    if jam < 10:
        pesan_akses = "Garasi Terbuka"
    else:
        pesan_akses = "Garasi Malam Terbuka, Lampu Dinyalakan"
elif pin % 2 == 0:  
    if (digit1 + digit3) == digit2:
        pesan_akses = "Garasi VIP Terbuka Khusus Bos"
    else:
        pesan_akses = "Kode Genap Ditolak, Alarm Berbunyi!"

status_cctv = "Mode Malam Merekam" if jam > 18 else "Mode Siang Standby"

print("\n--- STATUS SISTEM PINTU GARASI ---")
print(f"Digit 1: {digit1}, Digit 2: {digit2}, Digit 3: {digit3}")
print(f"Status Akses Pintu : {pesan_akses}")
print(f"Status Kamera CCTV : {status_cctv}")