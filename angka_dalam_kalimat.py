from terbilang import Terbilang

"""

Disini saya menggunakan library, untuk memudahkan pembuatan aplikasi
dan mempersingkat code.

"""

t = Terbilang()

angka = input("Masukkan sebuah angka (maks 4 digit) : ")

# Menerjemahkan angka inputan
t.parse(angka)

print(t.getresult())

"""

Sui Chan wa... kyou mo kawaii~~!

"""