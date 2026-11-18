def pelanggan (n):
    if n <=5:
        return 1
    else:
        return pelanggan(n - 1) + pelanggan(n - 2)
hari = int(input("masukkan hari ke-N: "))
print("jumlah pelanggan hari ke-", hari,"adalah", pelanggan(hari))

