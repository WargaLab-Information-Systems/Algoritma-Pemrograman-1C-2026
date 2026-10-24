total_belanja=int(input("total belanja:"))
if total_belanja % 100000==0:
    belanja="gratis"
    total_belanja=0

elif total_belanja % 50000==0:
    belanja="mendapat diskon 50%"
    total_belanja=total_belanja*50//100

elif total_belanja % 10000==0:
    belanja="mendapat diskon 20%"
    total_belanja=total_belanja*80//100

elif total_belanja >=200000:
    belanja="mendapat diskon 10%"
    total_belanja= total_belanja*90//100
else:
    belanja="harga normal"

status_poin="poin bertambah"if total_belanja>0 else"tidak ada poin"
print("total belanja awal:", belanja)
print("total bayar:", total_belanja)
print("status poin:", status_poin)
