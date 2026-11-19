undangan = set(input("Undangan: ").split(","))
webinar_a = set(input("Peserta A: ").split(","))
webinar_b = set(input("Peserta B: ").split(","))

print("Semua peserta: ", webinar_a | webinar_b)
print("Hadir keduanya: ", webinar_a & webinar_b)
print("Hanya salah satu: ", webinar_a ^ webinar_b)
print("Tidak hadir: ", undangan - (webinar_a | webinar_b))