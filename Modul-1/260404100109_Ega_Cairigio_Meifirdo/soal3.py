Jarak = 100
Konsumsi_per_liter = 40
Sisa_bensin = 1.5
Harga_per_liter = 10000

Jarak_total = Jarak * 2
Kebutuhan_bensin = Jarak_total / Konsumsi_per_liter
Bensin_harus_dibeli = Kebutuhan_bensin - Sisa_bensin
Total_biaya = Bensin_harus_dibeli * Harga_per_liter

print("Jarak total pulang-pergi =", Jarak_total, "km")
print("Kebutuhan bensin total =", Kebutuhan_bensin, "liter")
print("Bensin yang harus dibeli =", Bensin_harus_dibeli, "liter")
print("Total biaya beli bensin =", Total_biaya)