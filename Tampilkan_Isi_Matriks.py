elemen = [
    [1, 2, 3, 4, 5], 
    [6, 7, 8, 9, 10], 
    [11, 12, 13, 14, 15],
    [16, 17, 18, 19, 20]
     
    ]
baris = 4
kolom = 5

def tampil_matriks(n,m,a):
    for k in range(n):
        for l in range(m):
            print(a[k][l])

tampil_matriks(baris,kolom,elemen)