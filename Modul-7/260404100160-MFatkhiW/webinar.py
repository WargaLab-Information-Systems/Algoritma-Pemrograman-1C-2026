undangan = set()
webinar_a = set()
webinar_b = set()

while True:
    print("\n=== INPUT DATA UNDANGAN ===")
    nama = input("Masukkan nama undangan (ketik 'selesai' untuk berhenti): ").strip().title()

    if nama.lower() == "selesai":
        break
    elif nama == "":
        print("Nama tidak boleh kosong.")
    else:
        undangan.add(nama)


while True:
    if not undangan:
        print("\nDaftar undangan masih kosong.")
        break

    print("\n=== INPUT PESERTA WEBINAR A ===")
    nama = input("Masukkan nama peserta (ketik 'selesai' untuk berhenti): ").strip().title()

    if nama.lower() == "selesai":
        break
    elif nama == "":
        print("Nama tidak boleh kosong.")
    elif nama not in undangan:
        print("Nama tidak terdapat dalam daftar undangan.")
    else:
        webinar_a.add(nama)


while True:
    if not undangan:
        print("\nDaftar undangan masih kosong.")
        break

    print("\n=== INPUT PESERTA WEBINAR B ===")
    nama = input("Masukkan nama peserta (ketik 'selesai' untuk berhenti): ").strip().title()

    if nama.lower() == "selesai":
        break
    elif nama == "":
        print("Nama tidak boleh kosong.")
    elif nama not in undangan:
        print("Nama tidak terdapat dalam daftar undangan.")
    else:
        webinar_b.add(nama)


semua_peserta = webinar_a | webinar_b
hadir_keduanya = webinar_a & webinar_b
hanya_satu = webinar_a ^ webinar_b
tidak_hadir = undangan - semua_peserta


print("\n=== HASIL DATA WEBINAR ===")
print(f"Semua peserta dari kedua webinar: \n{semua_peserta}")
print(f"Peserta yang hadir di kedua webinar: \n{hadir_keduanya}")
print(f"Peserta yang hanya hadir di salah satu webinar: \n{hanya_satu}")
print(f"Undangan yang tidak hadir di webinar mana pun: \n{tidak_hadir}")