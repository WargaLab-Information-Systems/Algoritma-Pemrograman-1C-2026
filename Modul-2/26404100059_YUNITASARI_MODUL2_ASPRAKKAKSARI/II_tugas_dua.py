total = int(input('masukkan total belanj: '))
if  total % 100000 == 0:
    diskon = 100
elif  total % 50000 == 0:
    diskon = 50
elif total % 10000 == 0:
    diskon = 10 
elif total >= 200000:
    diskon = 10
else:
    diskon = 0
jumlah_diskon = total * diskon / 100
harga_akhir = total - jumlah_diskon
print('total belanja:', total )
print('diskon:', diskon, '%')
print('jumlah diskon:', jumlah_diskon)
print('harga akhir:', harga_akhir)

status_point = 'point bertambah' if  total > 0  else 'tidak ada point'
print(' status point:' ,status_point)
