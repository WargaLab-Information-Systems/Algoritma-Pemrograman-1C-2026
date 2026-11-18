def palindrom(kata):
    if kata == kata[::-1]:
        return True
    else:
        return False

kata = input("Masukkan sebuah kata: ")

if palindrom(kata):
    print(kata, "adalah kata palindrom")
else:
    print(kata, "bukan kata palindrom")
