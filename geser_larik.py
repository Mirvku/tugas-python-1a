# HALAMAN 26
nmax = 100 
a = []

def baca_larik(m,a):
    if m >= 100:
        print("Jumlah elemen harus di bawah 100")
        
    else:
        for index in range(int(m)):
            elemen = int(input(f"Masukkan elemen ke-{str(index)} : "))
            a.append(elemen)
    return a

def cetak_larik(m,a):
    print("CETAK LARIK")
    for indeks in range(m):
        print(a[indeks])
        
def geser_kanan(a):
    # Saya tidak menggunakan loop, karena menurut saya cara ini lebih simpel dan sama
    # seperti pada algoritma yang ada di PDF, code dibawah ini akan menjadikan nilai 
    # yang berada di akhir menjadi di urutan pertama atau index ke 0
    # dan menghapus nilai akhir sebelumnya, sehingga nilai yang ada pada list jadi tergeser
    # ke arah kanan.
    
    a.insert(0,a.pop())
    return f"Geser kanan : {a}"

def geser_kiri(a):
    a.append(a.pop(0))
    return f"Geser kiri : {a}"

n = int(input("Masukkan jumlah elemen larik : "))

baca_larik(n, a)

# Pilihan
print("Pilih salah satu : ")
print("1. Geser Kanan ")
print("2. Geser Kiri ")

pilihan = int(input("Pilih nomor : "))

if pilihan == 1:
    print(f"Sebelum geser kanan : {a}")
    print(f"Sesudah geser kanan {geser_kanan(a)}")
else:
    print(f"Sebelum geser kiri : {a}")
    print(f"Sesudah geser kiri {geser_kiri(a)}")

cetak_larik(n, a)
# print(a)


"""

Sui Chan wa... kyou mo kawaii~~!

"""