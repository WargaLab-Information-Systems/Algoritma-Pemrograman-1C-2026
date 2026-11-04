def palindrom(kata):
    kata = kata.lower()
    return kata == kata[::-1]


while True:
    kata = input("Masukkan sebuah kata: ").strip()
    if kata.isalpha():
        break
    print("Input harus berupa satu kata yang hanya berisi huruf, masukkan ulang.")

hasil = palindrom(kata)
print(f"Hasil fungsi: {hasil}")
if hasil:
    print(f"Kata '{kata}' adalah palindrom.")
else:
    print(f"Kata '{kata}' bukan palindrom.")
