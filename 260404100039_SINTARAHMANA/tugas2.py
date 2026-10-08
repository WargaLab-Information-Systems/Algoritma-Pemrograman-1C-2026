jarak = 100
konsumsi = 40
sisa_bensin = 1.5
harga_bensin = 10000

total_jarak = jarak*2
kebutuhan_bensin = total_jarak/konsumsi
bensin_beli = kebutuhan_bensin-sisa_bensin
biaya = bensin_beli*harga_bensin

print("total jarak=", total_jarak)
print("kebutuhan bensin=", kebutuhan_bensin)
print("bensin yang harus dibeli=", bensin_beli)
print("total biaya=", biaya)