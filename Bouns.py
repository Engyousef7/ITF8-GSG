L1 = int(input("Enter L1"))
L2 = int(input("Enter L2"))
L3 = int(input("Enter L3"))
H = int(input("Enter H"))

def Area(L1,H):
    Area = 0.5*L1*H
    return Area
print(Area(L1,H))

def perimeter(L1,L2,L3):
    perim = L1+L2+L3
    return perim
print(perimeter(L1,L2,L3))
