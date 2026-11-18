undangan = set()
webinar_a = set()
webinar_b = set()

while True:
    print("=MASUKAN UNDANGAN=")
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

    print("=NAMA PESERTA WEBINAR A=")
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

    print("=NAMA PESERTA WEBINAR B=")
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

print("\nSemua peserta dari kedua webinar:")
print(semua_peserta)

print("\nPeserta yang hadir di kedua webinar:")
print(hadir_keduanya)

print("\nPeserta yang hanya hadir di salah satu webinar:")
print(hanya_satu)

print("\nUndangan yang tidak hadir di webinar mana pun:")
print(tidak_hadir)