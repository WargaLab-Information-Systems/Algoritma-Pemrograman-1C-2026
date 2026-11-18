def palindrom(kata):
    if kata == kata[::-1]:
        return True
    else:
        return False

kata = input("Masukkan sebuah kata: ").lower()

if palindrom(kata):
    print(kata, "termasuk kata palindrom")
else:
    print(kata, "bukan kata palindrom")