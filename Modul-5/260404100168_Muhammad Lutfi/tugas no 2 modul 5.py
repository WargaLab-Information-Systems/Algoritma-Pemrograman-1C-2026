def palindrom(kata):
    return kata == kata[::-1]

kata = input("masukkan kata: ").lower()

if palindrom(kata):
    print("kata tersebut adalah palindrom")
else:
    print("kata tersebut bukan palindrom")
