print("=== Lampu Hias Belah Ketupat ==")
while True:
    n = int(input("Masukkan n tinggi setengah menara = "))
    if n >=2 and n <= 15:
        break
    print("TIDAK VALID, ULANG!!")
# ATAS
#Angka Naik
for baris in range(1, n + 1):
    print("  " * (n-baris), end="")
    for a in range(1, baris + 1):
        print(a % 10, end=" ")
    for b in range( baris - 1, 0, -1 ):
        print( b % 10, end=" ")
    print()
# BAWAH
#Angka Turun
for baris in range(n - 1, 0, -1 ):
    print("  " * (n-baris), end="")
    for a in range(1, baris + 1):
        print(a % 10, end=" ")
    for b in range(baris - 1, 0, -1 ):
        print(b % 10, end=" ")
    print()
    


