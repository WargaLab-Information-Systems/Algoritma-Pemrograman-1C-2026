print("===== Cek Palindrom =====")
def palindrom():
    kata = input("Masukkan kata (kata harus mengandung huruf kecil semua): ")
    kata_terbalik = ""
    for i in kata:
        kata_terbalik = i + kata_terbalik
        print("Kata terbalik : ", kata_terbalik)
    if kata == kata_terbalik:
        print("Kata termasuk : Palindrom")
        return True
    else:
        print("Kata termasuk : Bukan Palindroem")
        return False
palindrom()
