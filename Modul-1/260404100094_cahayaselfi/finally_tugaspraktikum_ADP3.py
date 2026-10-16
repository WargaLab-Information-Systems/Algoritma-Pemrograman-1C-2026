#BBM DIMAS - STATIS
jarak_satu_arah = 100 #km
konsumsi = 40 # km per liter
sisa_BBM = 1.5 #liter
harga_BBM = 10000 #rupiah per liter

#total jarak pulang pergi
total_jarak = jarak_satu_arah * 2
print(total_jarak)

total_bbm_butuh = total_jarak / konsumsi
print(total_bbm_butuh)

bbm_harus_beli = total_bbm_butuh - sisa_BBM
print(bbm_harus_beli)

total_biaya = bbm_harus_beli * harga_BBM
print(total_biaya)