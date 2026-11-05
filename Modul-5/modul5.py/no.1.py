def hitung_pelanggan(n):
    if n == 1:
        return 1
    else:
        if n == 2:
            return 1
        else:
            return hitung_pelanggan(n - 1) + hitung_pelanggan(n - 2)
n = int(input("Masukkan hari ke: "))
if n <0:
    print ("n harus bilangan bulat positif")
else:
    print("Jumlah pelanggan pada hari ke-", n, "adalah:", hitung_pelanggan(n))
for n in range (1, n+1):
    print(hitung_pelanggan(n), end="")