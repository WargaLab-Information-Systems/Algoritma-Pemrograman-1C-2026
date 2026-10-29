print("--- Program Dua Piramida Angka Saling Berhadapan ---")
n = int(input("Masukkan sebuah bilangan bulat positif (n): "))

for i in range(1, n + 1):
  for j in range(1, i + 1):
    print(j, end=" ")

  spasi = (n - i) * 4
  print(" " * spasi, end="")

  for j in range(i, 0, -1):
    print(j, end=" ")

  print()