undangan = set()
webinar_a = set()
webinar_b = set()

print("=== INPUT DATA UNDANGAN ===")
undangan = set(map(str.strip, input("Masukkan nama undangan (pisahkan dengan koma): ").split(",")))

print("\n=== PESERTA WEBINAR A ===")
webinar_a = set(map(str.strip, input("Masukkan peserta (pisahkan dengan koma): ").split(",")))

print("\n=== PESERTA WEBINAR B ===")
webinar_b = set(map(str.strip, input("Masukkan peserta (pisahkan dengan koma): ").split(",")))

print("\n=== HASIL DATA WEBINAR ===")
print("Semua peserta:", webinar_a | webinar_b)
print("Peserta kedua webinar:", webinar_a & webinar_b)
print("Peserta hanya satu webinar:", webinar_a ^ webinar_b)
print("Undangan yang tidak hadir:", undangan - (webinar_a | webinar_b))