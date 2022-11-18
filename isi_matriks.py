elemen = []
baris = 4
kolom = 5

# Membuat function isi_matriks untuk menambahkan elemen ke dalam List 2D
def isi_matriks(n,m,a):
    for i in range(n):
        elemen.append([])
        for j in range(m):
            tambah = int(input(f"Elemen baris-{str(i+1)} kolom-{str(j+1)}: "))
            a[i].append(tambah)
            
    return a

# Menambahkan argumen ke function isi_matriks 
isi_matriks(baris,kolom,elemen)

# Membuat function untuk menampilkan isi matriks
def tampil_matriks(n,m,a):
    for k in range(n):
        for l in range(m):
            print(a[k][l])

tampil_matriks(baris,kolom,elemen)

"""

Sui Chan wa... kyou mo kawaii~~!

"""