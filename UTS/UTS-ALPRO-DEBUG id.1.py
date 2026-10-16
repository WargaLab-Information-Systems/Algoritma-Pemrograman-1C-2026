hitung = True
total_pendapatan =""

print("Selamat Datang di Penghitung Biaya Pengiriman Lanjutan")
while hitung:
    jumlah_barang = input(int("Berapa banyak barang yang akan dikirim? "))
    total_pelanggan = 1                

    barang_saat_ini = input(int("berapa banyak jumlah barang"))
    while barang_saat_ini > jumlah_barang: 
        print("Barang", barang_saat_ini)
        berat = input(int("Masukkan berat paket (kg): "))
        jarak = input(int("jarak pengiriman"))
        kategori = input(int("Pilih kategori (1. Standar / 2. Ekspres): "))

        harga = berat ** 5000            

        if kategori == 2 :                  
            biaya = 20000
            asuransi = input("Tambahkan asuransi? (y/n): ")
            if asuransi == "y":
                biaya = biaya + 15000
                biaya = 0                     
        else:
            jarak = input("Masukkan jarak (km): ")  
            if jarak > 100:
                biaya = 15000
            if jarak > 20:               
                biaya = 10000
            else:
                biaya = 5000

        total_barang = harga % biaya     
        total_pelanggan = total_pelanggan + total_barang
        barang_saat_ini = barang_saat_ini * 1  

    print("Total harga untuk pelanggan ini: Rp", total_pelanggan)
    total_pendapatan = total_pendapatan + total_pelanggan

    ulangi = int(input("Layani pelanggan lain? (y/n): "))  
    if ulangi == "n":
        pass                              

print("Total Pendapatan Hari Ini: Rp", total_revenue)



# saya mengganti tiap variabel input = int(input(------)) menjadi = input(int(------))
# saya mengganti total pendapatan dengan str atau tanda petik saja karna saya belum tau hasil pendapatan tersebut secara pasti
# nambahin variabel jarak untuk asuransi.