# Membuat tiga set kosong
undangan = set()
webinar_A = set()
webinar_B = set()

# Mengisi daftar undangan
jumlah = int(input("Masukkan jumlah undangan: "))

for i in range(jumlah):
    nama = input("Masukkan nama undangan: ")
    undangan.add(nama)

# Mengisi peserta Webinar A
jumlah_A = int(input("Masukkan jumlah peserta Webinar A: "))

for i in range(jumlah_A):
    nama = input("Masukkan nama peserta: ")
    webinar_A.add(nama)

# Mengisi peserta Webinar B
jumlah_B = int(input("Masukkan jumlah peserta Webinar B: "))

for i in range(jumlah_B):
    nama = input("Masukkan nama peserta: ")
    webinar_B.add(nama)

# Menampilkan semua peserta kedua webinar
semua_peserta = webinar_A | webinar_B
print("Semua peserta:", semua_peserta)

# Menampilkan peserta yang hadir di kedua webinar
kedua_webinar = webinar_A & webinar_B
print("Peserta yang hadir di kedua webinar:", kedua_webinar)

# Menampilkan peserta yang hanya hadir di salah satu webinar
satu_webinar = webinar_A ^ webinar_B
print("Peserta yang hanya hadir di salah satu webinar:", satu_webinar)

# Menampilkan undangan yang tidak hadir di webinar mana pun
tidak_hadir = undangan - (webinar_A | webinar_B)
print("Undangan yang tidak hadir:", tidak_hadir)

