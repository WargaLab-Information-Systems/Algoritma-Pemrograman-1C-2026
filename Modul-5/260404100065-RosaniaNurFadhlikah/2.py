def is_palindrom(kata):
    return kata.lower() ==kata[::-1].lower() 

kata=input("masukkan kata:")
hasil=is_palindrom(kata)
    

if hasil:
    print(kata,"adalah palindrom")
else:
    print(kata,"bukan palindrom")