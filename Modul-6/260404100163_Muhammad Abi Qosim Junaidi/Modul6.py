# list = [1,2,3,"mangga"]
# list.append("durian")
# print(list)


# list = [1,2,3,"mangga"]
# # menghapus list menggunakan remove()
# list.remove("mangga")
# print(list)


# # menghapus list menggunakan del sesuai indeks
# del list[0]
# print(list)


# mobil = ("alphard","toyota","L300")
# print(mobil[1])


mobil = ("alphard","toyota","L300")
mobilanyar = mobil + ("volkswagen",)
print(mobilanyar)


angkaA = (4,5,6,7)
angka = (1,2,3)
del angka
print(angkaA)


tup = ("cincin","anting","gelang")
i = 0
while i < len(tup):
    print(tup[i])
    i=i+1


outfit = ("baju","celana","rok")
for i in outfit:
    for j in outfit:
        for k in outfit:
            print("kombinasi outfit hari ini",i,j,k)

matriks = [[10,20,30], # Baris 0
           [40,50,60], # Baris 1
           [70,80,90]] # Baris 2

matriks = [[10,20,30],
           [40,50,60],
           [70,80,90]]

elemen = matriks[1][2]
print("Elemen bari 1 kolom 2",elemen)

matriks[0][0] = 99
print("Matriks setelah diubah:",matriks[0])