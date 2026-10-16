pin = int(input('masukkan PIN 3 digit: '))
jam = int(input('masukkan jam kedatangan (0-23): '))

digit1 = pin // 100
digit2 = (pin // 10) % 10
digit3 = pin % 10

print("\n---HASIL PEMERIKSAAN---")
print('digit pertama: ', digit1)
print('digit kedua: ', digit2)
print('digit ketiga: ', digit3)

if pin % 5 == 0:
    if jam < 12:
        print('garasi pagi terbuka')
    else: 
        print('garasi malam berbuka')
        print('lampu dinyalakan')
elif pin % 2 == 0:
    if digit1 + digit3 == digit2:
        print("garasi VIP terbuka Khusus bos")
    else:
        print('kode genap di tolak, alarm berbunyi')
else: 
    print('akses di tolak sepenuhnya')

status_kamera = 'mode malam merekam' if jam > 18  else 'mode siang standby'

print('status kamera: ', status_kamera)

