def Nama_Bulan(bln):
    if bln == 1:
        return "Januari"
    
    elif bln == 2:
        return "Februari"
    
    elif bln == 3:
        return "Maret"
    
    elif bln == 4:
        return "April"
    
    elif bln == 5:
        return "Mei"
    
    elif bln == 6:
        return "Juni"
    
    elif bln == 7:
        return "Juli"
    
    elif bln == 8:
        return "Agustus"
    
    elif bln == 9:
        return "September"
    
    elif bln == 10:
        return "Oktober"
    
    elif bln == 11:
        return "November"
    
    elif bln == 12:
        return "Desember"

tanggal = int(input("Tanggal : "))
bulan   = int(input("Bulan   : "))
tahun   = int(input("Tahun   : "))

nama_bulan =  Nama_Bulan(bulan)

if bulan > 12 or bulan < 1 or tahun < 0 or tanggal < 0 or tanggal > 31:
    print("Oopsie... ERROR...")

else:
    print(f"{tanggal} - {nama_bulan} - {tahun}")
    
    
"""

Sui Chan wa... kyou mo kawaii~~!

"""