jumlah_beasiswa_penuh=0
for i in range(1,11):
    print("\nMahasiswa ke-",i)
    nama=input("nama mahasiswa:")
    ipk=float(input("ipk: "))
    if ipk<3.00:
        print("nama:",nama)
        print("tidak memenuhi syarat beasiswa karena ipk kurang dari 3.00")
        continue
    penghasilan= int(input("penghasilan orang tua per bulan:"))
    print("nama:", nama)
    print("ipk:", ipk)
    if penghasilan <=3000000:
        print("hasil seleksi:beasiswa penuh")
        jumlah_beasiswa_penuh+=1
        if jumlah_beasiswa_penuh == 3:
            print("kuota beasiswa penuh sudah terpenuhi!")
            break

    elif penghasilan <=5000000:
        print("hasil seleksi:beasiswa sebagian")
    else:
        print("hasil seleksi: tidak mendapat beasiswa ")
print("\njumlah penerima beasiswa penuh:",jumlah_beasiswa_penuh)
        