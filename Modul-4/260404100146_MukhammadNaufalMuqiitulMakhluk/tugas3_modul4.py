n = int(input("Masukkan angka: "))

# mengatur jumlah baris
for i in range(1, n + 1):

    # Mencetak angka dari kecil ke besar
    for j in range(i):
        print(j + 1, end="")

    # spasi antara dua piramida
    for j in range(2 * (n - i) + 3):
        print(" ", end="")

    # Mencetak angka dari besar ke kecil
    for j in range(i, 0, -1):
        print(j, end="")

    print()