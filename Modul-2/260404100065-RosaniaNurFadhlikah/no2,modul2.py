total_belanja=int(input("masukkan total belanja awal siti:"))


if total_belanja % 100000 ==0:

    diskon_persen=100

elif total_belanja % 50000==0:

    diskon_persen=50
   
elif total_belanja % 10000==0:

    diskon_persen=20
   
elif total_belanja >= 200000:

    diskon_persen=10
    
else:

    diskon_persen=0

jumlah_diskon= total_belanja*diskon_persen /100
total_bayar= total_belanja - jumlah_diskon


status_poin="poin bertambah" if total_bayar>0 else"tidak ada poin"
print("status poin:",status_poin)