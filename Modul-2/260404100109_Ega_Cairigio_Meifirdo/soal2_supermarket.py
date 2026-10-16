total_belanja = int(input("Masukkan total belanja:"))

if total_belanja % 100000 == 0:
    diskon = 100
elif total_belanja % 50000 == 0:
    diskon = 50
elif total_belanja % 10000 == 0:
    diskon = 20
elif total_belanja >= 200000:
    diskon = 10
else:
    diskon = 0 

total_bayar = total_belanja - (total_belanja * diskon / 100)

status_poin = "Poin Bertambah" if total_bayar > 0 else "Tidak Ada Poin"

print("Total belanja awal:", int(total_belanja))
print("Total harga akhir:", int(total_bayar))
print("Status Poin:", status_poin)