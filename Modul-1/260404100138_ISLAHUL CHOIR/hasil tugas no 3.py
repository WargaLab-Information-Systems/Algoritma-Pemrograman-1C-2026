jarak_sekali_jalan = 100     
konsumsi = 40                 
sisa_bensin = 1.5             
harga_per_liter = 10000       

#  Total jarak pulang-pergi
total_jarak = jarak_sekali_jalan * 2

#  Total kebutuhan bensin
total_bensin = total_jarak / konsumsi

# Bensin yang harus dibeli
bensin_dibeli = total_bensin - sisa_bensin

#  Total biaya
total_biaya = bensin_dibeli * harga_per_liter

print("Total jarak pulang-pergi =", total_jarak, "km")
print("Total kebutuhan bensin   =", total_bensin, "liter")
print("Bensin yang harus dibeli =", bensin_dibeli, "liter")
print("Total biaya bahan bakar = Rp", total_biaya)