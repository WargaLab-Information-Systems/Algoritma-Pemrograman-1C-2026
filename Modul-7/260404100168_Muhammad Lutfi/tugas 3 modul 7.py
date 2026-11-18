undangan = set()
webinar_a = set()
webinar_b = set()

print("=== DATA UNDANGAN ===")
jumlah = int(input("Jumlah undangan: "))

for i in range(jumlah):
    nama = input("Nama undangan: ")
    undangan.add(nama)

print("\n=== PESERTA WEBINAR A ===")
jumlah = int(input("Jumlah peserta: "))

for i in range(jumlah):
    nama = input("Nama peserta: ")
    webinar_a.add(nama)

print("\n=== PESERTA WEBINAR B ===")
jumlah = int(input("Jumlah peserta: "))

for i in range(jumlah):
    nama = input("Nama peserta: ")
    webinar_b.add(nama)

print("\n=== HASIL DATA WEBINAR ===")

print("Semua peserta:")
print(webinar_a | webinar_b)

print("\nPeserta yang hadir di kedua webinar:")
print(webinar_a & webinar_b)

print("\nPeserta yang hanya hadir di salah satu webinar:")
print(webinar_a ^ webinar_b)

print("\nUndangan yang tidak hadir:")
print(undangan - (webinar_a | webinar_b))