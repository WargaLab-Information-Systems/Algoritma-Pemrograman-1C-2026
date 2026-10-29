print("==== Belanja Ibu Siti ====")
Total_belanja_awal = int(input("Masukkan Total Belanja = Rp. "))
if Total_belanja_awal % 100000 == 0:
    print("Diskon = 100%")
    print("GRATIS!!")
    Besar_Diskon = Total_belanja_awal * 100 // 100
    print("Besar Diskon = Rp. ", Besar_Diskon)
    Total_bayar_setelah_diskon = Total_belanja_awal - Besar_Diskon
    print("Total bayar setelah diskon = Rp.",Total_bayar_setelah_diskon)
elif Total_belanja_awal % 50000 == 0:
    print("Diskon = 50%")
    Besar_Diskon = Total_belanja_awal * 50 // 100
    print("Besar Diskon = Rp. ", Besar_Diskon)
    Total_bayar_setelah_diskon = Total_belanja_awal - Besar_Diskon
    print("Total bayar setelah diskon = Rp.",Total_bayar_setelah_diskon)
elif Total_belanja_awal % 10000 == 0:
    print("Diskon = 20%")
    Besar_Diskon = Total_belanja_awal * 20 // 100
    print("Besar Diskon = Rp. ", Besar_Diskon)
    Total_bayar_setelah_diskon = Total_belanja_awal - Besar_Diskon
    print("Total bayar setelah diskon =  Rp.",Total_bayar_setelah_diskon)
elif Total_belanja_awal >= 200000:
    print("Diskon = 10%")
    Besar_Diskon = Total_belanja_awal * 10 // 100
    print("Besar Diskon = Rp. ", Besar_Diskon)
    Total_bayar_setelah_diskon = Total_belanja_awal - Besar_Diskon
    print("Total bayar setelah diskon = Rp.",Total_bayar_setelah_diskon)
else:
    print("Bayar harga normal")
    print("Total pembayaran", Total_belanja_awal)
print("Status = Poin Bertambah"if Total_bayar_setelah_diskon > 0 else "Status = Tidak ada poin" )
