def cek_palindrom(kata):
    kata = kata.lower()
    kembalikan = ""

    for huruf in kata:
        kembalikan = huruf + kembalikan

    if kata == kembalikan:
        return True
    else:
        return False

kata = input("Masukkan sebuah kata: ")
if cek_palindrom(kata):
    print("Kata", kata, "adalah kata palindrom.")
else:
    print("Kata", kata, "bukan kata palindrom.")