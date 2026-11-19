print("===== Pendataan inventaris PC =====")

def Layak_PC(status, ram):
    if Status == "Normal" and ram >= 8:
        return "PC layak"                                       #melempar keluar fungsi
    else:                                   
        return "PC tidak layak"

Data_PC = []
while True:
    Nama_PC = (input("Nama PC : "))
    if Nama_PC.lower() == "sudah":
        break
    Status = (input("Status : "))
    Kapasitas = (input("Kapasitas RAM : "))
    try:                                                        #menugji kode
        Kapasitas = int(Kapasitas)
        Kategori = Layak_PC(Status, Kapasitas)                  #memanggil fungsi cek status dan RAM
    except:                                                     #alternatif jika kode try error
        Kategori = "Format RAM Kacau"
    Data_PC.append([Nama_PC, Status, Kapasitas, Kategori])
print("Data inventaris PC : ", Data_PC)
