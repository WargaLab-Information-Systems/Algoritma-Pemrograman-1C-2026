def jumlah_pelanggan(n):
    if n==1 or n==2:
        return 1
    else:
        return jumlah_pelanggan(n-1) + jumlah_pelanggan(n-2)

n=int(input("masukkan hari:"))
hasil=jumlah_pelanggan(n)
print("jumlah hari ke",n,"adalah:",  hasil)