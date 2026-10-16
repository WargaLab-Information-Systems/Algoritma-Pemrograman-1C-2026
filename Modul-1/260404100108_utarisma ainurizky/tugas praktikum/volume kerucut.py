#Menghitung volume kerucut

r = float(input("Masukkan jari jari alas (cm): "))
tinggi = float(input("Masukkan tinggi kerucut (cm): "))

volume = (1/3) * 22/7 * r ** 2 * tinggi
print("volume kerucut adalah", round(volume, 2), "cm3")