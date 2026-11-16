while True:
    n = int(input("Masukkan tinggi menara (2-15), atau 0 untuk keluar: "))
    print("angka yang dimasukin:", n)
    if n == 0:
        print("Program selesai.")
        break

    if n < 2 or n > 15:
        print("Input tidak valid! Silakan masukkan angka 2-15.")
        continue
    for i in range(1, n + 1):
        print(" " * (n - i), end="")

        for j in range(1, i + 1):
            print(j % 10, end="")

        for j in range(i - 1, 0, -1):
            print(j % 10, end="")

        print()
   
    for i in range(n - 1, 0, -1):
        print(" " * (n - i), end="")

        for j in range(1, i + 1):
            print(j % 10, end="")

        for j in range(i - 1, 0, -1):
            print(j % 10, end="")
        print()

    print()