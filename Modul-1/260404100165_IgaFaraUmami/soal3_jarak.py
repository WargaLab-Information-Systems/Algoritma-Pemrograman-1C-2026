jarak = 100
konsumsi = 40
sisa_bensin = 1.5
harga_bensin = 10000

total_jarak = jarak * 2

kebutuhan_bensin = total_jarak / konsumsi

bensin_dibeli = kebutuhan_bensin - sisa_bensin

total_biaya = bensin_dibeli * harga_bensin

print("Total jarak perjalanan =", total_jarak, "km")
print("Total kebutuhan bahan bakar =", kebutuhan_bensin, "liter")
print("Bahan bakar yang harus dibeli =", bensin_dibeli, "liter")
print("Total biaya bahan bakar = Rp", total_biaya)