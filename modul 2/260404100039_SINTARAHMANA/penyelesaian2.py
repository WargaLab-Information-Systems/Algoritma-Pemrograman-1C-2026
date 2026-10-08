#program perhitungan diskon belanjaan siti

#input total belanja

total_belanja = int(input("masukkan total belanja: Rp"))

#menentukan diskon
if total_belanja % 100000==0:
    diskon = 100
elif total_belanja % 50000==0:
    diskon = 50
elif total_belanja % 10000==0:
    diskon = 20
elif total_belanja >= 200000 and total_belanja % 10000!=0:
    diskon = 10
else:
    diskon = 0

#menghitung potongan dan total bayar
jumlah_diskon = total_belanja*diskon/100
total_bayar = total_belanja-jumlah_diskon

#operator ternary untuk status point
status_poin = "poin bertambah" if total_bayar > 0 else "tidak ada poin"

#ouput hasil
print("===HASIL PERHITUNGAN===")
print("total belanja awal :", total_belanja)
print("diskon :", diskon, "%")
print("jumlah diskon :", jumlah_diskon)
print("total bayar :", total_bayar)
print("status poin :", status_poin)