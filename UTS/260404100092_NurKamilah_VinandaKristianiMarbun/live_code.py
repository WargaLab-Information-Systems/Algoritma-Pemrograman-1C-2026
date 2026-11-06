regular = 40000 #menyimpan harga tiket ke dalam variable
vip = 75000
vvip = 100000
tiket = '0' #menyimpan variable

while tiket: #perulangan tiket
    beli = int(input('beli tiket :(yyy jika pesanan cukup)'))##
    if beli == 'yyy':
        break
    tiket += 1
    print(beli)

if beli == regular:
    print('anda harus menambah minuman seharga Rp. 10000/tiket')
    minuman = int(input('pilih jenis minuman Y/y : '))
else :
    print("anda mendapat minuman gratis")

if tiket > 3:
    if 