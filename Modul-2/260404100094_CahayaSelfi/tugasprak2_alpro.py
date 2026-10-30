# Program hitung Diskon bu siti Supermarket "KOPERASI NDESO"

total_belanja = float(input("Masukkan total belanjaan (Rp): "))

if total_belanja % 100000 == 0: 
    diskon = 1.0  
elif total_belanja % 50000 == 0:
    diskon = 0.50  
elif total_belanja % 10000 == 0:
    diskon = 0.20  
elif total_belanja >= 200000:
    diskon = 0.10  
elif total_belanja >= 300000 :
    diskon = 0.5
else:
    diskon = 0.0  

total_bayar = total_belanja - (total_belanja * diskon)

poin_keanggotaan = (
    "Poin Bertambah" if total_bayar > 0 elif total bayar > 100000 print("tidak") else "Tidak Ada Poin"
)

print("\n--- RINCIAN PEMBAYARAN ---")
print(f"Total Belanja Awal : Rp{total_belanja: }")
print(f"Total Harga Akhir  : Rp{total_bayar: }")
print(f"Status Poin        : {poin_keanggotaan}")