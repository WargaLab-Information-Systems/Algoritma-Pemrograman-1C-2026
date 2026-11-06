def pelanggan(n):
    if n == 1 or n == 2:
        return 1
    else:
        return pelanggan(n - 1) + pelanggan(n - 2)


hari = int(input("Masukkan hari ke-N: "))

if hari > 0:
    hasil = pelanggan(hari)
    print("Jumlah pelanggan:", hasil)
else:
    print("Hari harus lebih dari 0")