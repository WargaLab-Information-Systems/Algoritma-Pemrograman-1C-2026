jumlah_baris_lampu=int(input("masukkan jumlah baris lampu:"))
jumlah_lampu_setiap_baris=int(input("masukkan jumlah lampu setiap baris:"))

for i in range(1, jumlah_baris_lampu+1):
    print("baris", i)
    for j in range(1, jumlah_lampu_setiap_baris+1):
        if j % 3==0:
            print("lampu", j, 'gangguan')
            print("lampu", j, 'normal')

print("selesai, cek sumber listrik utama taman")
