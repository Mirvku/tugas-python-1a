def tukar(a, r):
    b = a
    a = r
    r = b
    
    return f"A = {a} R = {r}"

a = int(input("Masukkan nilai a : "))
r = int(input("Masukkan nilai r : "))

print(tukar(a,r))