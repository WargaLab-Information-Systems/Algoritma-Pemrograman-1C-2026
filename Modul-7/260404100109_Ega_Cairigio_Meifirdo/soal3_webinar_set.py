def isi_himpunan(himpunan, keterangan):
    data = input(f"{keterangan} (pisahkan dengan koma): ")
    himpunan.update(map(str.strip, data.title().split(",")))
    himpunan.discard("")


def tampilkan(judul, himpunan):
    isi = ", ".join(sorted(himpunan)) or "(tidak ada)"
    print(f"{judul}: {isi}")


undangan = set()
webinar_a = set()
webinar_b = set()

isi_himpunan(undangan, "Daftar undangan")
isi_himpunan(webinar_a, "Peserta Webinar A")
isi_himpunan(webinar_b, "Peserta Webinar B")

semua_peserta = webinar_a.union(webinar_b)
hadir_keduanya = webinar_a.intersection(webinar_b)
hanya_satu = webinar_a.symmetric_difference(webinar_b)
tidak_hadir = undangan.difference(semua_peserta)

print("\n=== Hasil Pengolahan Data Webinar ===")
tampilkan("Semua peserta kedua webinar", semua_peserta)
tampilkan("Peserta yang hadir di keduanya", hadir_keduanya)
tampilkan("Peserta yang hanya hadir di satu webinar", hanya_satu)
tampilkan("Undangan tidak hadir di mana pun", tidak_hadir)
