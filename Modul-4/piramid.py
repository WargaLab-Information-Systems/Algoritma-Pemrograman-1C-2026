n = int(input("Masukkan nilai n: "))

for i in range(1, n + 1):
  
    for j in range(1, i + 1):
        print(j, end="")

    jarak = 2 * (n - i)
    print(" " * jarak, end="")

    for k in range(i, 0, -1):
        print(k, end="")
    
    print()