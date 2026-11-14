print("\n=== 2. PENJADWALAN SHIFT ASISTEN LAB ===")
asisten_awal = []

# Input asisten awal sampai 'cukup'
while True:
  nama = input("Masukkan nama asisten (ketik 'cukup' dengan huruf kecil): ")
  if nama == "cukup":
    break
  asisten_awal.append(nama)

# Dikunci permanen pakai tuple[cite: 2]
tuple_awal = tuple(asisten_awal)

# Tambah asisten baru & gabung ke wadah baru[cite: 2]
tambahan = input("Masukkan 1 asisten tambahan yang baru bergabung: ")
asisten_akhir = list(tuple_awal) + [tambahan]

# Input hari tugas sampai 'cukup'
hari_list = []
while True:
  h = input("Masukkan nama hari tugas (ketik 'cukup'): ")
  if h == "cukup":
    break
  hari_list.append(h)
tuple_hari = tuple(hari_list)

# Input pengecualian shift
print("\n--- Aturan Pengecualian ---")
exc_asisten = input("Nama asisten yang ada pengecualian: ")
exc_hari = input("Hari pengecualiannya: ")

# Cetak kombinasi shift
print("\n--- Jadwal Shift Asisten ---")
for a in asisten_akhir:
  for h in tuple_hari:
    # Lewati jika cocok dengan pengecualian[cite: 2]
    if a == exc_asisten and h == exc_hari:
      continue
    print(f"Asisten: {a} | Hari: {h}")