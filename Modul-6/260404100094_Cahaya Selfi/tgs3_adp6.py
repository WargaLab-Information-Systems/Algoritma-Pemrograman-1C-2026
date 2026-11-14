print("\n=== 3. PENDATAAN INVENTARIS PC ===")


# Fungsi kustom tanpa try-except, menggunakan .isdigit() untuk cek apakah RAM berupa angka
def cek_kelayakan(status, ram):
  # Jika input RAM berupa teks (seperti 'Delapan'), langsung kembalikan Format RAM Kacau[cite: 2]
  if not ram.isdigit():
    return "Format RAM Kacau"

  # Evaluasi jika status 'Normal' dan RAM minimal 8[cite: 2]
  if status == "Normal" and int(ram) >= 8:
    return "Layak"
  else:
    return "Tidak Layak"


jumlah_pc = int(input("Masukkan jumlah PC yang ingin didata: "))
inventaris = []

# Input data ke dalam multidimensional list[cite: 2]
for i in range(jumlah_pc):
  print(f"\nData PC ke-{i+1}")
  nama_pc = input("Nama PC: ")
  status_pc = input("Status (Wajib ketik 'Normal' atau 'Rusak'): ")
  ram_pc = input("Kapasitas RAM (GB): ")
  inventaris.append([nama_pc, status_pc, ram_pc])

print("\n--- Hasil Evaluasi PC ---")
for pc in inventaris:
  nama = pc[0]
  status = pc[1]
  ram = pc[2]

  # Memanggil fungsi evaluasi
  kelayakan = cek_kelayakan(status, ram)

  # Cetak murni string dengan format persis permintaan soal (bukan dictionary)[cite: 2]
  print(f'{{ "PC": "{nama}", "Status": "{kelayakan}" }}')