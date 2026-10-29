print("=== Pola Piramida ===")
n = int(input("Masukkan n untuk tinggi piramida = "))
for baris1 in range(1, n+1):
    for a in range(1, baris1 + 1):
        print(a, end=" ")
    for spasi in range((n-baris1) * 2 + 1):
        print(" ", end=" ")
    for d in range(baris1, 0, -1):
        print(d, end=" ")
    print()
for baris2 in range(n-1, 0, -1):
    for b in range(1, baris2 + 1):
        print(b, end=" ")
    for spasi in range((n-baris2) * 2 + 1):
        print(" ", end=" ")
    for c in range(baris2, 0, -1):
        print(c, end=" ")
    print()

