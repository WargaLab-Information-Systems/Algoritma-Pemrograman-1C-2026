#Soal 2 
# total_belanja = 500000

# print("Total belanja awal:", total_belanja)

# if total_belanja % 100000 == 0:
#     total_bayar = 0
# elif total_belanja % 50000 == 0:
#     total_bayar = total_belanja * 50 // 100
# elif total_belanja % 10000 == 0:
#     total_bayar = total_belanja * 80 // 100
# elif total_belanja >= 200000:
#     total_bayar = total_belanja * 90 // 100
# elif total_belanja >= 300000:
#     total_bayar = total_belanja * 40 // 100
# else:
#     total_bayar = total_belanja

# print("Total harga akhir:", total_bayar)

# poin = "Poin Bertambah" if total_bayar > 0 else "Tidak Ada Poin"
# print("Status poin:", poin)

# #Soal 3
# suhu = 1200
# tekanan = 60

# print("Suhu:", suhu, "derajat")
# print("Tekanan:", tekanan, "Bar")

# if suhu > 1000:
#     if tekanan > 50:
#         print("MELTDOWN! SEGERA EVAKUASI!")
#     else:
#         print("Bahaya Suhu: Segera Turunkan Daya!")
# elif suhu > 500:
#     if tekanan > 30:
#         print("Tekanan Tidak Stabil")
#     else:
#         print("Operasi Reaktor Normal")
# else:
#     print("Reaktor Belum Cukup Panas")

# # pompa = "Pompa Maksimal" if suhu > 800 else "Pompa Normal"
# # print("Status pompa:", pompa)
# if suhu >800:
#     pompa = "Pompa Maksimal"
# else:
#     pompa = "Pompa Normal"  

#Soal 4
pin = -246
jam = 10

digit1 = pin // 100
digit2 = (pin // 10) % 10
digit3 = pin % 10

print("Digit pertama:", digit1)
print("Digit kedua:", digit2)
print("Digit ketiga:", digit3)

if pin % 5 == 0:
    if jam < 12:
        print("Garasi Pagi Terbuka")
    else:
        print("Garasi Malam Terbuka, Lampu Dinyalakan")
elif pin % 2 == 0:
    if digit1 + digit3 == digit2:
        print("Garasi VIP Terbuka Khusus Bos")
    else:
        print("Kode Genap Ditolak, Alarm Berbunyi!")
else:
    print("Akses Ditolak")

cctv = "Mode Malam Merekam" if jam > 18 else "Mode Siang Standby"
print("Status CCTV:", cctv)
