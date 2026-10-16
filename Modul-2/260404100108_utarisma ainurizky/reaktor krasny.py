# Reaktor Krasny
suhu = int(input("Masukkan suhu (Celcius): "))
tekanan = int(input("Masukkan tekanan (Bar): "))
print("Suhu: ", suhu, "Tekanan: ", tekanan)

if suhu > 1000:
    if tekanan > 50:
       print("MELTDOWN! SEGERA EVAKUASI!")
    else:
        print("Bahaya Suhu: Segera Turunkan Daya!")
elif suhu > 500:
    if tekanan > 30:
        print("Tekanan Tidak Stabil")
    else:
        print("Operasi Reaktor Normal")
else:
    print("Reaktor Belum Cukup Panas")

pompa = "Pompa Maksimal" if suhu > 800 else "Pompa Normal"
print("Status pompa: ", pompa)