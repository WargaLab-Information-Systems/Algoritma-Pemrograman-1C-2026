# Soal 3 - Webinar (pakai set)
undangan = set()
webinar_a = set()
webinar_b = set()

# isi set lewat input, pisahkan nama dengan koma
data = input("Daftar undangan (pisah koma): ")
for nama in data.split(","):
    undangan.add(nama.strip())

data = input("Peserta Webinar A (pisah koma): ")
for nama in data.split(","):
    webinar_a.add(nama.strip())

data = input("Peserta Webinar B (pisah koma): ")
for nama in data.split(","):
    webinar_b.add(nama.strip())

# operasi himpunan
print("\nSemua peserta kedua webinar:", webinar_a | webinar_b)
print("Hadir di keduanya:", webinar_a & webinar_b)
print("Hanya hadir di salah satu:", webinar_a ^ webinar_b)
print("Undangan yang tidak hadir di mana pun:", undangan - (webinar_a | webinar_b))