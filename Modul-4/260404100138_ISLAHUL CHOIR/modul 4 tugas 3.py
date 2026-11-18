
n = int(input("Masukkan jumlah baris: "))

if n <= 0:
    print("Masukkan bilangan bulat positif!")
else:
    for i in range(1, n + 1):

        for j in range(1, i + 1):
            print(j, end=" ")

        for spasi in range(2 * (n - i) + 1):
            print("  ", end="")

        for j in range(i, 0, -1):
            print(j, end=" ")

        print()
