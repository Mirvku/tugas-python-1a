a = [5,4,6,8,3,2]

def geser_kanan(a):
    # Saya tidak menggunakan loop, karena menurut saya cara ini lebih simpel dan sama
    # seperti pada algoritma yang ada di PDF, code dibawah ini akan menjadikan nilai 
    # yang berada di akhir menjadi di urutan pertama atau index ke 0
    # dan menghapus nilai akhir sebelumnya, sehingga nilai yang ada pada list jadi tergeser
    # ke arah kanan.
    
    a.insert(0,a.pop())
    return a

print(f"Nilai awal : {a}")
print(f"Nilai setelah di geser ke kanan: {geser_kanan(a)}")


"""

Sui Chan wa... kyou mo kawaii~~!

"""