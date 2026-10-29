print("=== Seleksi awal penerima beasiswa ===")
Banyak_mahasiswa = 10
Jumlah_mahasiswa_beasiswa_penuh = 0
for i in range(10):
    Nama = input("Nama = ")
    IPK = float(input("IPK = "))
    Penghasilan = int(input("Penghasilan orang tua = "))
    if IPK < 3.00:
        print("Status = TIDAK MEMENUHI SYARAT")
        continue
    else:
        if Penghasilan <= 3000000:
            if Jumlah_mahasiswa_beasiswa_penuh < 3:
                print("Status = Beasiswa Penuh")
                Jumlah_mahasiswa_beasiswa_penuh = Jumlah_mahasiswa_beasiswa_penuh + 1
                print("Jumlah mahasiswa beasiswa penuh = ", Jumlah_mahasiswa_beasiswa_penuh)
            else:
                print("Status = Beasiswa Sebagian (Kuota beasiswa penuh full)")       
        elif Penghasilan <= 5000000:
            print("Status = Beasiswa Sebagian")
        else:
            print("Status = Tidak Layak Mendapat Beasiswa")
