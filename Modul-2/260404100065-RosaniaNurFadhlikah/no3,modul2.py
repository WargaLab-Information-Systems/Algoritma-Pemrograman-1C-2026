suhu=int(input("masukkann suhu reaktor(celcius):"))
tekanan=int(input("masukkan tekanan gas(bar):"))


if suhu > 1000:
    if tekanan > 50:
        status ="meltdown! segera evakuasi!"
    else:
        status="bahaya suhu: segera turunkan daya"
elif suhu > 500:
    if tekanan > 30:
        status="tekanan tidak stabil"
    else:
        status="operasi reaktor normal"
else:
    status="reaktor belum cukup panas"

pompa = "pompa maksimal" if suhu > 800 else "pompa normal" 


if suhu >800:
    print("pompa maksimal")
else:
    print("pompa normal")

    print("===status reaktor===")
    print("suhu reaktor:", suhu)
    print("tekanan gas:", tekanan)
    print("status bahaya:", status)