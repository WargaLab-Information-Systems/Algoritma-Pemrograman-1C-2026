def pelanggan(Z):
    if Z == 1 or Z == 2:
        return 1
    return pelanggan(Z - 1) + pelanggan(Z - 2)


while True:
    hari = int(input("Masukkan hari ke: "))
    if hari > 0:
        break
    print("Z harus bilangan bulat positif, masukkan ulang.")

print(f"Jumlah pelanggan pada hari ke {hari}: {pelanggan(hari)} orang")
