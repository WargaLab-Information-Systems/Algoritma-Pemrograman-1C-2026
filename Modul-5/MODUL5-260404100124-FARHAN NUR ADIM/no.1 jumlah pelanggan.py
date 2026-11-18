def pelanggan (hari):
    if hari == 1 or hari ==2:
        return 1
    else:
        return pelanggan (hari - 1) + pelanggan (hari - 2)

while True:
    hari = int(input("Masukkan hari ke-N: "))
    if hari > 0:
        print(f"\nJumlah pelanggan hari ke-{hari} adalah {pelanggan(hari)} orang")
        break
    else:
        print ("\nMasukkan bilangan bulat positif! (selain 0)")