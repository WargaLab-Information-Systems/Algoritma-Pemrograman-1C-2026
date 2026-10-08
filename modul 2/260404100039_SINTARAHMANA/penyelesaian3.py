#program pemantauan reaktor nuklir

#input suhu
suhu = int(input("masukkan suhu reaktor(celcius):"))
tekanan = int(input("masukkan tekanan gas(bar):"))

#menentukan status bahaya reaktor

if suhu > 1000:
    if tekanan > 50:
        status = "MELDOWN! SEGERA EVAKUASI"
    else:
        status = "bahaya suhu:segera turunkan daya!"

elif suhu > 500:
    if tekanan > 30:
        status = "tekanan tidak stabil"
    else:
        status = "operasi reaktor normal"

else:
    status = "reaktor belum cukup panas"

#operator ternary untuk status pompa air
#status_pompa = "pompa maksimal" if suhu > 800 else "pompa normal"

if suhu >800:
    print("pompa maksimal")
elif suhu <800:
    print("pompa normal")

#ouput hasil
print("===STATUS REAKTOR===")
print("suhu reaktor :", suhu)
print("tekanan tugas :", tekanan)
print("status bahaya :", status)
#print("status pompa air :", status_pompa)