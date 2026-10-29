print("=== Menghitung Gaji Mingguan ===")
Total_Gaji = 0
Gaji_pokok = 100000
for i in range(7):
    print(f"---- Hari ke {i+1} ----")
    Total_Gaji = Total_Gaji + Gaji_pokok
    print("Total gaji sementara = ", Total_Gaji)

    Shift_malam = input("Shift malam (y/n) = ")
    while True:
       Jam_lembur = int(input("Jam lembur = "))
       if (Jam_lembur >= 0 and Jam_lembur <= 3) or Jam_lembur == 4 or Jam_lembur == 6 or Jam_lembur == 8:
            break
       else: 
            print("INPUT JAM LEMBUR TIDAK VALID!!")
    if Shift_malam == "y":
        Tambahan_upah = 50000
        print("Tambahan Upah = ", Tambahan_upah)
        Total_Gaji = Total_Gaji + Tambahan_upah
        print("Total gaji sementara = ", Total_Gaji)
    
    if Jam_lembur == 0:
        pass
    elif Jam_lembur > 0 and Jam_lembur <= 3:
        Upah1 = 25000
        print("Mendapat upah sebesar", Upah1)
        Total_Gaji = Total_Gaji + Upah1
        print("Total gaji sementara = ", Total_Gaji)
    elif Jam_lembur == 4:
        Upah2 = 100000
        print("Mendapat upah sebesar", Upah2)
        Total_Gaji = Total_Gaji  + Upah2
        print("Total gaji sementara = ", Total_Gaji)
    elif Jam_lembur == 6:
        Upah3 = 200000
        print("Mendapat upah sebesar", Upah3)
        Total_Gaji = Total_Gaji + Upah3
        print("Total gaji sementara = ", Total_Gaji)
    elif Jam_lembur == 8:
        Upah4 = 300000
        print("Mendapat upah sebesar", Upah4)
        Total_Gaji = Total_Gaji + Upah4
        print("Total gaji sementara = ", Total_Gaji)
    else:
        print("Jumlah lembur melebihi batas")
print("Total gaji 1 minggu = Rp. ", Total_Gaji)
