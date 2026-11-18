jarak = 100
konsumsi_bensin_liter = 40
sisa_bensin = 1.5
harga_bensin = 10000	
total_jarak = jarak + jarak
total_kebutuhan_bensin = total_jarak / konsumsi_bensin_liter
total_biaya = total_kebutuhan_bensin * harga_bensin
jumlah_bensin_yang_dibeli = total_kebutuhan_bensin - sisa_bensin
print("Total kebutuhan bensin:", total_kebutuhan_bensin, "liter")
	
print("total jarak pulang-pergi:", total_jarak, "km")
print("total_kebutuhan_bensin=", total_kebutuhan_bensin, "liter")
print("jumlah biaya bensin yang dibeli Rp:", jumlah_bensin_yang_dibeli * harga_bensin)
print("jumlah bensin yang dibeli:", jumlah_bensin_yang_dibeli, "liter")
