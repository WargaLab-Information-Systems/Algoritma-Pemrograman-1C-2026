undangan = set()
peserta_a = set()
peserta_b = set()

print("PROGRAM DATA PESERTA WEBINAR")

data = input("nama undangan (pisahkan dengan koma): ")
undangan = set(data.split(","))

data = input("peserta Webinar A (pisahkan dengan koma): ")
peserta_a = set(data.split(","))

data = input("peserta Webinar B (pisahkan dengan koma): ")
peserta_b = set(data.split(","))

semua_peserta = peserta_a | peserta_b
print("\nsemua peserta:", semua_peserta)

peserta_keduanya = peserta_a & peserta_b
print("peserta yang hadir di kedua webinar:", peserta_keduanya)

peserta_satu = peserta_a ^ peserta_b
print("peserta yang hanya hadir di salah satu webinar:", peserta_satu)

tidak_hadir = undangan - (peserta_a | peserta_b)
print("undangan yang tidak hadir:", tidak_hadir)