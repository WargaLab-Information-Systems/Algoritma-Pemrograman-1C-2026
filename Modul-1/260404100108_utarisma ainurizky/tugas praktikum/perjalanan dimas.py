# Perjalanan Dimas

jarak = float(input("Masukkan jarak pulang pergi (km): "))
konsumsi = float(input("Masukkan konsumsi bahan bakar (km per liter): "))
sisa_bensin = float(input("Masukkan sisa bensin (liter): "))
harga = float(input("Masukkan harga bahan bakar per liter (Rp): "))

jarak_total = jarak * 2
kebutuhan = jarak_total / konsumsi
dibeli = kebutuhan - sisa_bensin
biaya = dibeli * harga

print("Total jarak pulang pergi adalah", jarak_total, "km")
print("Total kebutuhan bahan bakar", kebutuhan, "liter")
print("Bahan bakar yang harus dibeli", dibeli, "liter")
print("Total biaya bahan bakar adalah Rp", round(biaya))
