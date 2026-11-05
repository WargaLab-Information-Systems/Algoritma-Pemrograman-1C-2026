def cek_palindrom(kata):
    if kata == kata[::-1]:
        return True
    else:
        return False

kata = input("masukkan sebuah kata:")

if cek_palindrom(kata):
    print(kata, "merupakan kata palindrom")
else:
    print(kata, "bukan kata palindrom")

