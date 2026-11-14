print("=== 1. PENDAFTARAN KLUB ROBOTIKA ===")
anggota = []

while True:
  nama = input(
      "Masukkan nama calon anggota (ketik 'selesai' dengan huruf kecil): "
  )
  if nama == "selesai":
    break
  anggota.append(nama)

print("\n--- Status Validitas Nama ---")
for nama in anggota:
  if nama == "admin" or len(nama) < 4:
    print(f"- {nama}: Tidak valid")
  else:
    print(f"- {nama}: Valid")

penyusup = input(
    "\nMasukkan nama penyusup yang mau dihapus (ketik pas): "
)
if penyusup in anggota:
  anggota.remove(penyusup)
  print(f"Sukses! '{penyusup}' berhasil dihapus.")
else:
  print(f"'{penyusup}' tidak ditemukan, program tetap aman (tidak crash).")

print("Daftar anggota akhir:", anggota)