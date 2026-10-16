Regular = 40000
VIP = 75000
VVIP = 100000
Uang = 0
Total_tagihan = 0
Jumlah_tiket = 0
Minuman = ""
Pelanggan = ""

while True:
    Tiket = input("Pilih tiket apa yang anda beli/Jika sudah cukup ketik N : ")
    # memasukkan pilihan tiket "jika user mengimputkan N" maka dia sudah cukup membeli tiketnya 
    if Tiket == "Regular":
        print ("Apakah anda ingin menambah minuman seharga Rp.10.000?")
        Minuman = input("Y/N : ")
        # memasukkan pilihan apakah user mau membeli minuman dengan pilihan "Y/N"
        Jumlah_tiket += 1
        if Minuman != "Y":
            print("Anda tidak membeli minuman")            
        else:
            print("Anda membeli minuman tambahan")
    elif Tiket == "VIP":
        print("Anda mendapatkan minuman gratis")
        Jumlah_tiket += 1
    elif Tiket == "VVIP":
        print("Anda mendapatkan minuman gratis")
        Jumlah_tiket += 1
    else:
        print("Anda membeli tiket sebanyak ", Jumlah_tiket )
        #menghitung total tiket yang di beli user
        if Jumlah_tiket == 3:
            Pelanggan = input("Apakah Kamu member : ")
            if Pelanggan == "Iya":
                Uang * 15/100
                Uang = input("Bayar : ")
                #membayar
        else:
            Uang * 10/100
        Uang = input("Bayar : ")