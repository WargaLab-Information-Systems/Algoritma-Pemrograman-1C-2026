#Belanja Siti
total = int(input("Masukkan total belanja: "))
print("total belanja awal: ", total)

if total % 100000 == 0:
    bayar = 0
elif total % 50000 == 0:
    bayar = total - total * 50 / 100
elif total % 10000 == 0:
    bayar = total - total * 20 / 100
elif total >= 200000 == 0:
    bayar = total - total * 10 / 100
else:
    bayar = total
print("Total yang harus dibayar: ", bayar)

poin = "Poin Bertambah" if bayar > 0 else "Tidak Ada Poin"
print("Status Poin: ", poin)