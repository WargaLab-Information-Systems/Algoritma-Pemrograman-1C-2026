n = int(input("Masukkan bilangan bulat positif n: "))
jarak = 4

for z in range(1, n + 1):
    for zh in range(z, 0, -1):
        print(zh % 10, end=' ')

    for s in range(2 * (n - z)):
        print(' ', end=' ')

    for sh in range(jarak):
        print(' ', end='')

    for zh in range(1, z + 1):
        print(zh % 10, end=' ')
    print()