elemen = []
baris = 4
kolom = 5

def isi_matriks(n,m,a):
    for i in range(n):
        elemen.append([])
        for j in range(m):
            tambah = int(input(f"Elemen baris-{str(i+1)} kolom-{str(j+1)}: "))
            a[i].append(tambah)
    return a
            
# Menambahkan argumen ke function isi_matriks 
print(isi_matriks(baris,kolom,elemen))

"""

Sui Chan wa... kyou mo kawaii~~!

"""