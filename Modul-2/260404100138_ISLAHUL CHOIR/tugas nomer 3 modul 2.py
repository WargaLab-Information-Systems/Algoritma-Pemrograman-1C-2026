# Input suhu dan tekanan
suhu = float(input("Masukkan suhu reaktor (C): "))
tekanan = float(input("Masukkan tekanan gas (Bar): "))

# Percabangan bersarang untuk menentukan bahaya
if suhu > 1000:
    if tekanan > 50:
        status = "MELTDOWN! SEGERA EVAKUASI!"
    else:
        status = "Bahaya Suhu: Segera Turunkan Daya!"
elif suhu > 500:
    if tekanan > 30:
        status = "Tekanan Tidak Stabil"
    else:
        status = "Operasi Reaktor Normal"
else:
    status = "Reaktor Belum Cukup Panas"

# Ternary operator untuk pompa
pompa = "Pompa Maksimal" if suhu > 800 else "Pompa Normal"

# Output
print("Suhu :", suhu, "C")
print("Tekanan :", tekanan, "Bar")
print("Status Bahaya :", status)
print("Status Pompa :", pompa)