pin = int(input("masukkan 3 digit PIN:"))
jam = int(input("masukkan jam kedatangan (0-23):"))


digit1 = pin//100
digit2 = (pin//10) % 10
digit3 = pin % 10


if pin % 5:
    if jam <12:
        status_pintu = "garasi pagi terbuka"
    else:
        status_pintu = "garasi malam terbuka"
elif pin % 2==0:
    if digit1 + digit3==digit2:
        status_pintu = "garasi VIP terbuka khusus bos"
    else:
        status_pintu = "kode genap ditolak, alarm berbunyi!"
else:
    status_pintu = "akses ditolak sepenuhnya"


status_kamera = "mode malam merekam" if jam >= 18 else "mode siang stanby"


print("===STATUS GARASI===")
print("digit pertama :", digit1)
print("digit kedua :", digit2)
print("digit ketiga :", digit3)
print("status pintu :", status_pintu)
print("status kamera :", status_kamera)