suhu = float(input("Masukkan Suhu Reaktor (°C): "))
tekanan = float(input("Masukkan Tekanan Gas (Bar): "))

if suhu > 1000:
    if tekanan > 50:
        pesan_bahaya = "MELTDOWN! SEGERA EVAKUASI!"
    if suhu > 20:
        pesan_bahaya = "Reaktor Belum Panas"
    else:
        pesan_bahaya = "Bahaya Suhu: Segera Turunkan Daya!"
elif suhu > 500:
    if tekanan > 30:
        pesan_bahaya = "Tekanan Tidak Stabil"
    else:
        pesan_bahaya = "Operasi Reaktor Normal"
else:
    pesan_bahaya = "Reaktor Belum Cukup Panas"
    

status_pompa = "Pompa Maksimal" if suhu > 800 else "Pompa Normal"

print("\n--- STATUS REAKTOR NUKLIR ---")
print(f"Suhu Reaktor    : {suhu} °C")
print(f"Tekanan Gas     : {tekanan} Bar")
print(f"Pesan Bahaya    : {pesan_bahaya}")
print(f"Status Pompa Air: {status_pompa}")