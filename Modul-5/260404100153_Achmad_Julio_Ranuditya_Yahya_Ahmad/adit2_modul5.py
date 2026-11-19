def palindrom(kata):
    if kata == kata[::-1]:
        return True
    else:
        return False

# Input kata dari pengguna
kata = input("Masukkan sebuah kata: ")

# Menampilkan hasil
if palindrom(kata):
    print(kata, "adalah kata palindrom")
else:
    print(kata, "bukan kata palindrom")