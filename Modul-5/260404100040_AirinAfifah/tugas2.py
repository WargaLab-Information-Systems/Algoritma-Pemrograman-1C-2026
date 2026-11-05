kata = input("masukkan kata: ")
def cek_palindrom(kata):
    if kata == kata[::-1]:
        return True
    else:
        return False

if cek_palindrom(kata):
    print(kata, "termasuk palindrom")
else:
    print(kata, "bukan palindrom")