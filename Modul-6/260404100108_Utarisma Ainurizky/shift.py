awal = []
while True:
    nama = input("Asisten awal: ")
    if nama == "cukup":
        break
    awal.append(nama)
awal = tuple(awal)

tambahan = input("Asisten tambahan: ")
asisten = awal + (tambahan, )

hari = []
while True:
    h = input("Hari tugas: ")
    if h == "cukup":
        break 
    hari.append(h)
hari = tuple(hari)

ex_asisten = input("Asisten pengecualian: ")
ex_hari = input("Hari pengecualian: ")

for a in asisten:
    for h in hari:
        if a == ex_asisten and h == ex_hari:
           continue
        print(a, "-", h)