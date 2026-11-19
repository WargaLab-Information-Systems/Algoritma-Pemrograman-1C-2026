while True:
    n = int(input("Masukkan tinggi menara (2-15): "))

    if n >= 2 and n <= 15:
        break
    print("Input salah, masukkan angka 2 sampai 15!")

# Bagian atas menara
for baris in range(1, n + 1):
    print(" " * (n - baris), end="")

    for angka in range(1, baris + 1):
        print(angka % 10, end="")

    for angka in range(baris - 1, 0, -1):
        print(angka % 10, end="")

    print()

# Bagian bawah menara
for baris in range(n - 1, 0, -1):
    print(" " * (n - baris), end="")

    for angka in range(1, baris + 1):
        print(angka % 10, end="")

    for angka in range(baris - 1, 0, -1):
        print(angka % 10, end="")

    print()