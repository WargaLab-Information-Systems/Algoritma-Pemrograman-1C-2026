barang = input(str("masukkan nama barang :"))

reguler = 40
VIP = 75
VVIP = 100
minuman = 10
while barang <= 1:

    if reguler >= 40 :
        print(reguler+minuman)
    elif VIP >= 75 :
        print("mendapatkan minuman secara gratis")
    elif VVIP >= 100 :
        print("mendapatkan minuman gratis") 