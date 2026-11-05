baris = int(input("masukkan baris lampu:"))
lampu = int(input("masukkan jumlah lampu:"))

for i in range (1, baris+1):
    print("baris ke-", i )
   
    for j in range (1, lampu+1):
        if j % 3 == 0:
            print("lampu", j ,"mengalami gangguan")
        else:
            print("lampu", j ,"berfungsi dengan normal")

print("memeriksa sumber listrik utama taman.")