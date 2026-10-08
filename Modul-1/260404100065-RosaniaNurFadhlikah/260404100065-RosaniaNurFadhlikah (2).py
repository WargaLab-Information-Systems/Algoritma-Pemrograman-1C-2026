jarak_rumah= 100
bahan_bakar_motor= 40
sisa_bahan_bakar= 1.5 
harga_spbu= 10000

total_jarak_pulang_pergi= jarak_rumah*2
total_bahan_bakar= total_jarak_pulang_pergi/bahan_bakar_motor
beli_bensin=total_bahan_bakar-sisa_bahan_bakar
total_biaya=beli_bensin*harga_spbu

print("total jarak pulang pergi=",total_jarak_pulang_pergi)
print("total bahan bakar=", total_bahan_bakar)
print("beli bensin=",beli_bensin)
print("total biaya=",total_biaya)