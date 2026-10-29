print("==== Menentukan suhu reaktor nuklir ====")
Suhu = float(input("Suhu reaktor: "))
Tekanan_gas = float(input("Tekanan gas bar: "))
if Suhu > 1000 and Tekanan_gas > 50:
    print("MELTDOWN! SEGERA EVAKUASI!")
elif Suhu > 1000 and Tekanan_gas <= 50:
    print("Bahaya Suhu: Segera Turunkan Daya!")
elif Suhu > 500 and Tekanan_gas > 30:
    print("Tekanan Tidak Stabil")
elif Suhu > 500:
    print("Operasi Reaktor Normal")
else:
    print("Reaktor Belum Cukup Panas")
print("Pompa Maksimal"if Suhu > 800 else "Pompa Normal")