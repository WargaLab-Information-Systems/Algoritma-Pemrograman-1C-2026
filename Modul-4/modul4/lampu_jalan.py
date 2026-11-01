while True:
    jumlah_baris = int(input("jumlah baris lampu: "))
    if jumlah_baris > 0:
        break
    print("jumlah harus lebih dari 0")
while True:
    jumlah_lampu = int(input("jumlah lampu:"))
    if jumlah_lampu > 0:
        break
    print("Jumlah lampu harus lebih dari 0")

for i in range(1, jumlah_baris+1):
    print(f"\nPemeriksaan baris ke-{i}")
    for j in range(1,jumlah_lampu+1):
        if j % 3==0:
            print(f"lampu{j}:mengalami gangguan")
        else:
            print(f"lampu{j}: berfungsi normal")
print("\nPeriksa sumber listrik utama taman!")