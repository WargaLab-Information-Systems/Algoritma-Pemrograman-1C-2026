jarak=100
jarak_per_liter=40
bensin_sisa=1.5
harga_bensin=10000

total_jarak=jarak*2
total_bensin=total_jarak/jarak_per_liter
bensin_dibeli=total_bensin-bensin_sisa
total_biaya=bensin_dibeli*harga_bensin

print("total jarak perjalanan =  ", total_jarak, "km")
print("total kebutuhan bensin=   ", total_bensin, "liter")
print("bensin yang harus dibeli= ", bensin_dibeli, "liter")
print("total biaya=", total_biaya)
