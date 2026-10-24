jarak=100
tangki_motor=40
sisa=1.5
harga=10000
jarak_pp= jarak*2
print(jarak_pp)

bensin_dimas_pp=jarak_pp / tangki_motor
print(bensin_dimas_pp)

bensin_yang_wajib_dibeli=bensin_dimas_pp-sisa
print(bensin_yang_wajib_dibeli)

uang_yang_harus_dibayar=bensin_yang_wajib_dibeli*harga
print(uang_yang_harus_dibayar)