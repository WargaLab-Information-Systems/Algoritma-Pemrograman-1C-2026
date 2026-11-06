def bayar_matcha(jumlah, topping="tidak"):
    harga = jumlah * 20000
    if topping == "boba":
        harga = harga + 5000
    elif topping == "krim":
        harga = harga + 3000
    return harga

while True:
    jumlah = int(input("Mau berapa gelas? "))
    if jumlah <= 0:
        print("Jumlah tidak valid, input ulang!")
        continue
    break
topping = input("Topping (boba/krim/tidak): ")

total = bayar_matcha(jumlah, topping)
print("Total bayar: Rp", total)