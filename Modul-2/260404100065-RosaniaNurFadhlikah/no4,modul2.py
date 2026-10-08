pin = int(input("Masukkan 3 digit kode PIN: "))
jam = int(input("Masukkan jam kedatangan (0-23): "))

digit_pertama = pin // 100
digit_kedua = (pin // 10) % 10
digit_ketiga = pin % 10

if pin % 5 :
    if jam < 12:
        status_pintu= "Garasi Pagi Terbuka"
    else: 
        status_pintu= "Garasi Malam Terbuka"

elif pin % 2 == 0:
    if (digit_pertama + digit_ketiga) == digit_kedua:
        status_pintu=("Garasi VIP Terbuka Khusus Bos")
    else:
        status_pintu=("Kode Genap Ditolak, Alarm Berbunyi!")

else:
    status_pintu=("Akses Ditolak Sepenuhnya")

status_cctv = "Mode Malam Merekam" if jam > 18 else "Mode Siang Standby"

print("status garasi")
print("digit pertama :", digit_pertama)
print("digit kedua:", digit_kedua)
print("digit ketiga:", digit_ketiga)
print("status pintu:", status_pintu)
print("status cctv:",status_cctv)
