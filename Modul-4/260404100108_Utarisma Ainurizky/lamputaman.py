baris = int(input("Jumlah baris: "))
lampu = int(input("Jumlah lampu: "))

for i in range(1, baris + 1 ):
    for j in range(1, lampu + 1 ):
        if j % 3 == 0:
            print("baris", i, "lampu, j, gangguan")
        else:
            print("baris", i, "lampu, j, normal")

print("Periksa sumber listrik utama taman")