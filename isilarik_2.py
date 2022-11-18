n = 100
a = []

def baca_larik(m,a):
    if m >= 100:
        return "Jumlah elemen harus di bawah 100"
    else:
        for index in range(int(m)):
            elemen = int(input(f"Masukkan elemen ke-{str(index)} : "))
            a.append(elemen)
        return a
    
        
k = int(input("Masukkan jumlah elemen larik ( < 100 ) : "))
print(f"Isi elemen A : {baca_larik(k,a)}")


"""

Sui Chan wa... kyou mo kawaii~~!

"""