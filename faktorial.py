def faktor(a):
    if a <= 1:
        return 1
    else:
        return a * (a-1)
    
a = int(input("Masukkan angka : "))

# Memproses faktor
for i in range(a+1):
    print(f"{str(i)} != {faktor(i)}")
    

"""

Sui Chan wa... kyou mo kawaii~~!

"""