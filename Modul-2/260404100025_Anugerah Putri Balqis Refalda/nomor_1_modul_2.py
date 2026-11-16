angka=int(input("masukkan angka:"))
digit1=angka//100
digit2=(angka//10)%10
digit3=angka%10
print(digit1, digit2, digit3)
print("digit1:",digit1)
print("digit2:",digit2)
print("digit3:",digit3)
nilai_pelacak=( digit1 * digit3)
if digit2 %2==0:
    bilangan= "bilangan ganjil"
    nilai_pelacak=nilai_pelacak+25
else:
    bilangan= "bilangan genap"
    nilai_pelacak=nilai_pelacak-digit2
print("bilangan:",bilangan)
print("nilai pelacak:",nilai_pelacak)

if nilai_pelacak % 3==0:
    nilai_pelacak=nilai_pelacak//3
else:
    nilai_pelacak=nilai_pelacak*2
print("nilai akhir:",nilai_pelacak)
if nilai_pelacak >=50:
    status_password=("kategori A")
elif nilai_pelacak >=20:
    status_password=("kategori B")
else:
    status_password=("password ditolak")
print("status password:",status_password)