# Mengimport package yg dibutuhkan.
import time
import math as mtk

# Function aplikasi
def menu():
    print("#"*50)
    print("#"+" "*48+"#")
    print("#"+" "*10+"Aplikasi Empat Persegi Panjang"+" "*8+"#")
    print("#"+" "*48+"#")
    print("#"*50)
    print("#"+" "*48+"#")
    print("#\t1. Hitung Luas"+" "*27+"#")
    print("#\t2. Hitung Keliling"+" "*23+"#")
    print("#\t3. Hitung Diagonal"+" "*23+"#")
    print("#\t4. Exit"+" "*34+"#")
    print("#"+" "*48+"#")
    print("#"*50)

def baca_dimensi():
    # Function ini tidak di gunakan!
    panjang = int(input("Masukkan panjang persegi : "))
    lebar   = int(input("Masukkan lebar persegi panjang : ")) 
    
def hitung_luas():
    print("#"*50)
    print("#"+" "*48+"#")
    print("#"+" "*18+"Hitung Luas"+" "*19+"#")
    print("#"+" "*48+"#")
    print("#"*50)
    print() # Untuk menambahkan enter
    
    # Input data
    panjang = float(input("Masukkan panjang persegi : "))
    lebar   = float(input("Masukkan lebar persegi panjang : ")) 
    luas    = round(panjang * lebar, 2)
    
    print() # Untuk menambahkan enter
    return tampil_hasil(1, luas)

def hitung_keliling():
    print("#"*50)
    print("#"+" "*48+"#")
    print("#"+" "*15+"Hitung Keliling"+" "*18+"#")
    print("#"+" "*48+"#")
    print("#"*50)
    print() # Untuk menambahkan enter
    
    # Input data
    panjang = int(input("Masukkan panjang persegi : "))
    lebar   = int(input("Masukkan lebar persegi panjang : ")) 
    keliling    = 2 * (panjang + lebar)
    
    print() # Untuk menambahkan enter
    return tampil_hasil(2, keliling)

def hitung_diagonal():
    print("#"*50)
    print("#"+" "*48+"#")
    print("#"+" "*15+"Hitung Diagonal"+" "*18+"#")
    print("#"+" "*48+"#")
    print("#"*50)
    print() # Untuk menambahkan enter
    
    # Input data
    panjang = int(input("Masukkan panjang persegi : "))
    lebar   = int(input("Masukkan lebar persegi panjang : ")) 
    diagonal= round(mtk.sqrt((panjang ** 2) + ( lebar ** 2)), 2)
    
    print() # Untuk menambahkan enter
    return tampil_hasil(3, diagonal)

def tampil_hasil(pilihan, nilai):
    if pilihan == 1:
       print(f"Luas persegi panjang = {nilai} cm2\n")
       time.sleep(1.8)
   
    elif pilihan == 2:
        print(f"Keliling persegi panjang = {nilai} cm\n")
        time.sleep(1.8)
    
    elif pilihan == 3:
        print( f"Diagonal persegi panjang = {nilai} cm\n")
        time.sleep(1.8)


while True:
    # Menampilkan menu
    menu()
    print() # Untuk menambahkan enter

    # Membuat inputan untuk memilih yang ada di menu
    pilihan = int(input("Masukkan pilihan anda : "))
    print() # Untuk menambahkan enter

    if pilihan == 1:
        hitung_luas()
        
    elif pilihan == 2:
        hitung_keliling()

    elif pilihan == 3:
        hitung_diagonal()
        
    elif pilihan == 4:
        print("Selesai... sampai jumpa! ")
        break
    
    else:
        print("Pilihan salah, Ulangi ! ")
        time.sleep(1.3)
    



"""

DIBUAT OLEH : Justin Anditiaman (50422764) 

Sui Chan wa... kyou mo kawaii~~!

"""