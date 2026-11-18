total = int(input("Masukkan total belanja: Rp "))
print("Total belanja awal: Rp", total)

if total % 100000 == 0:
    bayar = 0                  
elif total % 50000 == 0:
    bayar = total * 0.5        
elif total % 10000 == 0:
    bayar = total * 0.8        
elif total >= 200000:
    bayar = total * 0.9        
else:
    bayar = total              

print("Total bayar: Rp", bayar)

status = "Poin Bertambah" if bayar > 0 else "Tidak Ada Poin"
print("Status poin:", status)