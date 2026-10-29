print("=== Lampu Taman ==")
while True:
    a = int(input("Jumlah Baris Lampu : "))
    if a > 0:
        break
    print("Jumlah baris lampu harus lebih dari 0! Silakan coba lagi")
while True:
    b = int(input("Jumlah Lampu Setiap Baris: "))
    if b > 0:
        break
    print("Jumlah lampu harus lebih dari 0! Silakan coba lagi")
for Baris in range(1, a+1):
    for Banyak_lampu in range(1, b+1):
        if Banyak_lampu % 3 == 0:
            print(f"Baris: {Baris}, Lampu ke- {Banyak_lampu}, Lampu mengalami gangguan")
        else:
            print(f"Baris: {Baris}, Lampu ke- {Banyak_lampu}, Lampu normal")
print("==== Pemeriksaan lampu selesai, silakan periksa sumber listrik yang digunakan!! ====")