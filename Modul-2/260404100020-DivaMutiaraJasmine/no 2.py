total = int(input("Masukkan total belanja: Rp "))

if total % 100000 == 0:
    bayar = 0
elif total % 50000 == 0:
    bayar = total * 50 / 100
elif total % 10000 == 0:
    bayar = total * 80 // 100
elif total >= 200000:
    bayar = total * 90 / 100
else:
    bayar = total

poin = "Poin Bertambah" if bayar > 0 else "Tidak Ada Poin"

print("Total belanja awal: Rp", total)
print("Total yang harus dibayar: Rp", bayar)
print("Status poin:", poin)