def pelanggan(n):
    if n <= 2:
        return 1
    else:
        return pelanggan(n-1) + pelanggan(n-2)
n = int(input("Masukkan hari ke-: "))
print("jumlah pelanggan hari ke", n, "=",pelanggan(n))