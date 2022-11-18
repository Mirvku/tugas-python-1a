a = [5,4,6,8,3,2]

def geser_kiri(a):
    a.append(a.pop(0))
    return a

print(f"Nilai awal : {a}")
print(f"Nilai setelah di geser ke kiri: {geser_kiri(a)}")


"""

Sui Chan wa... kyou mo kawaii~~!

"""