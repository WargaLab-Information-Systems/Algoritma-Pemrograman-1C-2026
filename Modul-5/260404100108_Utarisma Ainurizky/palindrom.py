def palindrom(kata):
    return kata == kata[::-1]

kata = input("Masukkan kata: ")
if palindrom(kata):
    print(kata, "adalah palindrom (True)")
else:
    print(kata, "bukan palindrom (False)")