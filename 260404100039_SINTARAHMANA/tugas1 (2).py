def fibonacci(n):
    if n == 1 or n == 2:
        return 1
    else:
        return fibonacci(n - 1) + fibonacci(n-2)

n = int(input("masukkan hari ke- n:"))

for hari in range(1,n + 1):
    print("jumlah pelanggan hari ke-", hari, "adalah", fibonacci(hari))