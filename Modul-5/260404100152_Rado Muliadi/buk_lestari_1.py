def fibonacci(n):
    if n <= 2:
        return 1
    return fibonacci(n - 1) + fibonacci(n - 2)

N = int(input("Masukkan hari ke-N : "))
if N < 1:
    print("N harus berupa bilangan bulat positif")
else:
    print("Jumlah pelanggan pada hari ke-" + str(N) + " adalah", fibonacci(N), "orang") 
