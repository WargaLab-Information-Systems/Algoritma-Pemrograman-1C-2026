regular = 40000
vip = 75000
vvip = 100000
harga_minuman = 10000
jumlah_regular = 0
jumlah_vip = 0
jumlah_vvip = 0
total_minuman= 0

while True:
    jenis_tiket = str(input("Pilih jenis tiket yang dibeli (regular/vip/vvip): "))
    jumlah = int(input("Masukkan jumlah yang ingin dibeli: "))
    break

    if jenis_tiket == regular:
        jenis_regular += jumlah
    elif jenis_tiket == vip:
        jenis_vip += jumlah
    elif jenis_tiket == vvip:
        jenis_vvip += jumlah

    if jumlah_regular > 0:
        minuman = str(input("Apakah anda ingin menambah minuman seharga 10 ribu/tiket (Y/N): "))
        if minuman == "Y":
            total_minuman += jumlah_regular
        else:
            continue

#hanya sampai nomor soal 3