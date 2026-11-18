undangan = set()
webinar_a = set()
webinar_b = set()

def isi_himpunan(himpunan, keterangan):
    print("Masukkan", keterangan,)
    while True:
        nama = input("  Nama : ").title()
        if nama.lower() == "selesai":
            break
        if nama != "":
            himpunan.add(nama)

def tampil(judul, himpunan):
    if len(himpunan) == 0:
        print(judul, ": -")
    else:
        print(judul, ":", ", ".join(sorted(himpunan)))

isi_himpunan(undangan, "daftar undangan")
isi_himpunan(webinar_a, "peserta Webinar A")
isi_himpunan(webinar_b, "peserta Webinar B")

print("\n=== HASIL OLAH DATA WEBINAR ===")
tampil("Semua peserta kedua webinar    ", webinar_a | webinar_b)
tampil("Hadir di kedua webinar         ", webinar_a & webinar_b)
tampil("Hanya hadir di salah satu      ", webinar_a ^ webinar_b)
tampil("Undangan tidak hadir di mana pun", undangan - (webinar_a | webinar_b))
