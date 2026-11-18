undangan = set()
webinar_a = set()
webinar_b = set()

print("===== DATA UNDANGAN =====")
jumlah = int(input("Masukkan jumlah undangan: "))

for i in range(jumlah):
    nama = input("Masukkan nama undangan: ")
    undangan.add(nama)

print("\n===== PESERTA WEBINAR A =====")
jumlah = int(input("Masukkan jumlah peserta Webinar A: "))

for i in range(jumlah):
    nama = input("Masukkan nama peserta: ")
    webinar_a.add(nama)

print("\n===== PESERTA WEBINAR B =====")
jumlah = int(input("Masukkan jumlah peserta Webinar B: "))

for i in range(jumlah):
    nama = input("Masukkan nama peserta: ")
    webinar_b.add(nama)

# Menggabungkan peserta kedua webinar
semua_peserta = webinar_a.union(webinar_b)

# Peserta yang hadir di kedua webinar
keduanya = webinar_a.intersection(webinar_b)

# Peserta yang hanya hadir di salah satu webinar
salah_satu = webinar_a.symmetric_difference(webinar_b)

# Undangan yang tidak hadir di webinar mana pun
tidak_hadir = undangan.difference(semua_peserta)

print("\n===== HASIL DATA WEBINAR =====")

print("Semua peserta:", semua_peserta)

print("Peserta yang hadir di kedua webinar:", keduanya)

print("Peserta yang hanya hadir di salah satu webinar:", salah_satu)

print("Undangan yang tidak hadir:", tidak_hadir)