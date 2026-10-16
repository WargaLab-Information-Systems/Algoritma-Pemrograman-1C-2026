# Program untuk menghitung volume kerucut nomor 2

r = 7
t = 12

volume = (1/3) * 3.14 * (r ** 2) * t
print("Jari-jari alas :", r, "cm")
print("Tinggi :", t, "cm")
print("Volume :", volume, "cm³")    

# Program untuk nomor 3

jarak_satu_arah = 100
konsumsi_per_liter = 40
sisa_bensin_tangki = 1.5
harga_per_liter = 10000
total_jarak = jarak_satu_arah * 2
total_bensin_digunakan = total_jarak / konsumsi_per_liter   
besin_yang_dibeli = total_bensin_digunakan - sisa_bensin_tangki
total_biaya = besin_yang_dibeli * harga_per_liter  
print("Jarak_satu_arah :", jarak_satu_arah, "km")
print("Total jarak perjalanan PP :", total_jarak, "km")
print("Total kebutuhan bahan bakar :", total_bensin_digunakan, "liter")
print("Bahan bakar yang dibeli :", besin_yang_dibeli, "liter")
print("Total biaya pembelian_bensin :", total_biaya, "rupiah")   