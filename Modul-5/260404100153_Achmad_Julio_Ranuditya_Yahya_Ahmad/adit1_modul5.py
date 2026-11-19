def fibonacci(n):
    if n == 1 or n == 2:
        return 1
    else:
        return fibonacci(n-1) + fibonacci(n-2)

# Input jumlah hari
hari = int(input("Masukkan hari ke-: "))

# Menampilkan hasil
if hari > 0:
    print("Jumlah pelanggan pada hari ke-", hari, "adalah:", fibonacci(hari))
else:
    print("Masukkan bilangan positif!")