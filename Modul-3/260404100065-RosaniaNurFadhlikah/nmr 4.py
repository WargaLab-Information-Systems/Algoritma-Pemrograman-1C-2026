beasiswa_penuh=0
for i in range(1, 11):
    print("Mahasiswa ke -", i)
    
    nama =input("Nama : ")
    ipk =float (input("IPK : "))
    gaji =float(input("Penghasilan orang tua : "))
    
    
    if ipk < 3.00:
        print("Hasil untuk", nama, ": TIDAK MEMENUHI SYARAT")
        print("Lanjut ke mahasiswa selanjutnya ")
        continue  
    

    if gaji <= 3000000:
        print("Hasil untuk", nama, ": MENDAPAT BEASISWA PENUH")
        beasiswa_penuh = beasiswa_penuh + 1 
        print("")
        
       
        if beasiswa_penuh == 3:
            print("Kuota beasiswa penuh sudah 3 orang, seleksi dihentikan!")
            break 
    
    elif gaji <= 5000000:
        
        print("Hasil untuk", nama, ": MENDAPAT BEASISWA SEBAGIAN ")
    
    else:
        
        print("Hasil untuk", nama, ": TIDAK MENDAPAT BEASISWA ")

print("Program Selesai")
print("Total yang dapat beasiswa penuh:", beasiswa_penuh)