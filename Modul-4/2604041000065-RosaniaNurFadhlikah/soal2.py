gaji_perhari=100000
total_gaji=0
total_hari_lembur=0

for i in range(1,8):
    print("hari ke-", i)

    if total_hari_lembur >= 2:
        print("jatah lembur 2 hari sudah habis, hari ini tdk bisa lembur")
        lembur=0
    else:
        lembur=int(input("jam lembur:"))

        while lembur <0 or lembur >8:
            print("jam lembur salah! ulangg")
            lembur=int(input("jam lembur:"))
    
    if lembur >0:
        total_hari_lembur +=1
    
    if lembur > 8:
        print("lebih 8 jam tidak dihitung")
        uang_lembur=0
    if lembur==1:
        uang_lembur=25000
    elif lembur==2:
        uang_lembur=50000
    elif lembur==3:
        uang_lembur=75000
    elif lembur==4:
        uang_lembur=100000
    elif lembur==6:
        uang_lembur=200000
    elif lembur==8:
        uang_lembur=300000
    else:
        print("jam lembur tidak dihitung")
        uang_lembur=0

    shift_malam=input("shift malam? y/n:")

    gaji=gaji_perhari + uang_lembur
    if shift_malam== "y":
        gaji=gaji+50000

    print("gaji hari ini", gaji)
    total_gaji=total_gaji+gaji

print("total gaji 7 hari", total_gaji )

