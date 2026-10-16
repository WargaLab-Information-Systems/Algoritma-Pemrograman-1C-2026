#if

nilai = 80

if nilai >= 75:
    print("Lulus")

#if-else

nilai = 60

if nilai >= 75:
    print("Lulus")
else:
    print("Tidak Lulus")

#if-elif-else

nilai = 85

if nilai >= 90:
    print("A")
elif nilai >= 75:
    print("B")
else:
    print("C")

#nested if

nilai = 85
kehadiran = 90

if nilai >= 75:
    if kehadiran >= 80:
        print("Lulus")

bilangan = int(input("Masukkan bilangan: "))

if bilangan % 2 == 0:
    print("Bilangan Genap") 
else:
    print("Bilangan Ganjil")  

nomor_acak = 7
print('Tebak nomor acak dari 1-10')
tebakan = int(input('Masukkan tebakan: '))  
if tebakan == nomor_acak:
    print('Selamat!Tebakan Anda Benar')
    print('Tapi Tidak Ada Hadiah Untuk Anda :) ')
elif tebakan < nomor_acak:
    print('Tebakan Anda Terlalu Kecil')
else:
    print('Tebakan Anda Terlalu Besar')
    print('selesai')

a = int(input("Masukkan umur: "))
if a <= 15 :
    print("Muda")
elif a <= 22 :
    print("Remaja") 
else :
    print("Tua") 

nilai = int(input("Masukkan nilai: "))
if nilai >= 75:
    print("Lulus")
else:
    print("Tidak Lulus") 

total = 0
jumlah_tugas = 0

while True:
    nilai = int(input("Masukkan nilai tugas (-99 untuk selesai): "))
    if nilai == -99:
        break
    total = total + nilai
    jumlah_tugas = jumlah_tugas + 1

print("Total nilai tugas:", total)
print("Jumlah tugas:", jumlah_tugas)
