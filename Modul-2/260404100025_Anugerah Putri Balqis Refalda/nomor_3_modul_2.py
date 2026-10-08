suhu=int(input("masukkan suhu:"))
tekanan=int(input("masukkan tekanan gas:"))
if suhu>=1000:
    if tekanan>=50:
        peringatan="MELTDOWN! SEGERA EVAKUASI"
    else:
        peringatan="bahaya suhu: segera turunkan daya"
elif suhu>500:
    if suhu>=30:
        peringatan="tekanan tidak stabil"
elif suhu <=500:
    peringatan="reaktor normal"
else:
    peringatan="reaktor belum cukup panas"
print("peringatan:", peringatan )
    
pompa="pompa maksimal"if suhu>800 else"pompa normal"
print("status pompa:", pompa)
print("suhu:",suhu)
print("pesan status bahaya:", peringatan)
print("tekanan:",tekanan)