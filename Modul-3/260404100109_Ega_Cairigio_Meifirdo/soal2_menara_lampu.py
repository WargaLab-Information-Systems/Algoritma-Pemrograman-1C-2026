while True:
    tinggi = int(input("Tinggi setengah menara (2-15): "))
    if 2 <= tinggi <= 15:
        break
    print("Di luar rentang, ulangi!")

for baris in range(1, 2 * tinggi):
    if baris <= tinggi:
        panjang = baris
    else:
        panjang = 2 * tinggi - baris

    for spasi in range(tinggi - panjang):
        print(" ", end="")

    for angka in range(1, panjang + 1):
        print(angka % 10, end="")

    for angka in range(panjang - 1, 0, -1):
        print(angka % 10, end="")

    print()