print("=== Menghitung jarak perjalanan ===")
Jarak = 100
Konsumsi_BBM = 40 
Sisa_BBM = 1.5
Harga_BBM = 10000
Total_jarak_PP = Jarak + Jarak
print("Total jarak Pulang-Pergi = ", Total_jarak_PP)
Kebutuhan_BBM = Total_jarak_PP / Konsumsi_BBM
print("Kebutuhan BBM = ", Kebutuhan_BBM)
Total_BBM = Kebutuhan_BBM - Sisa_BBM
print("Total BBM yang harus dibeli = ", Total_BBM)
Total_biaya = Total_BBM * Harga_BBM
print("Total biaya = ", Total_biaya)