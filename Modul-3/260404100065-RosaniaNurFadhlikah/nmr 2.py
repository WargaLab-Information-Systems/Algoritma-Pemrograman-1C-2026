n = int(input("masuk tinggi setengah menara 2-15: "))

while n < 2 or n > 15:
    print("salah, harus 2-15")
    n = int(input("masuk tinggi setengah menara 2-15: "))

for i in range(1, n+1):
    spasi = " " * (n - i)
    
    angka = ""
    for j in range(1, i+1):
        angka = angka + str(j%10)
    for j in range(i-1, 0, -1):
        angka = angka + str(j%10)
    
    print(spasi + angka)

for i in range(n-1, 0, -1):
    spasi = " " * (n - i)
    
    angka = ""
    for j in range(1, i+1):
        angka = angka + str(j%10)
    for j in range(i-1, 0, -1):
        angka = angka + str(j%10)

    print(spasi + angka)

