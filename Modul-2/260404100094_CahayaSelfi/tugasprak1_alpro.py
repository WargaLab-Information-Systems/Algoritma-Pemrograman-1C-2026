password = input("Masukkan 3 digit password: ")

kode = int(password)
digit1 = kode // 100
digit2 = (kode // 10) % 10
digit3 = kode % 10

nilai_pelacak = digit1 * digit3

if digit2 % 2 != 0:  
    nilai_pelacak += 25
else:  
    nilai_pelacak -= digit2

pelacak_tahap1 = nilai_pelacak

if pelacak_tahap1 % 3 == 0:  
    nilai_akhir = pelacak_tahap1 // 3
else:  
    nilai_akhir = pelacak_tahap1 * 2

if nilai_akhir > 50:
    status_password = "Kategori A"
elif nilai_akhir > 20:
    status_password = "Kategori B"
else:
    status_password = "Password Ditolak"

if nilai_akhir % 2 == 0:
    siklus = "Siklus Genap"
else:
    siklus = "Siklus Ganjil"

print("\n--- HASIL ANALISIS BRANKAS ---")
print(f"Digit Pertama : {digit1}")
print(f"Digit Kedua   : {digit2}")
print(f"Digit Ketiga  : {digit3}")
print(f"Pelacak Awal  : {digit1 * digit3}")
print(f"Pelacak Tahap 1: {pelacak_tahap1}")
print(f"Nilai Akhir (Tahap 2): {nilai_akhir}")
print(f"Status Password: {status_password}")
print(f"Siklus        : {siklus}")